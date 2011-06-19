#!/usr/bin/python -O

# dust-example.py A Python GStreamer example with Qt
# Copyright (C) 2011 Nick Daniels <nick@dustv.org>
# Website: http://www.dustv.org

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.


import sys, os, platform
import gobject, pygst
pygst.require('0.10')
import gst
from PyQt4.QtCore import SIGNAL, SLOT
from PyQt4.QtGui import QApplication, QMainWindow, QPushButton, \
					QFileDialog

# Load converted GUI file
from mainUi import *

# Global Variables for Mixer Setup.
num_channels = 6
max_num_channels = 20
video_width = 853
video_height = 480
video_framerate = 24

#### MAIN APP CLASS ####
class MainApp(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)

		# Load GUI (from class in the mainUi.py file)
		self.uim = Ui_MainWindow()
		self.uim.setupUi(self)

		# Setup the video widgets in the GUI ready for video overlay
		(videoWidgets, self.videoBorders) = self.setupVideoWidgets()

		# Setup the pipeline manager and create the pipeline
		self.pipeM = PipelineManager()
		self.pipeM.createPipeline(self.uim, videoWidgets, self.videoBorders)

		# Connect the "Choose File" button to the choose_file callback
		self.connect(self.uim.chooseFile, SIGNAL('clicked()'), self.choose_file)

		# Set channel 1 as currently selected
		self.pipeM.setPrevSelected(1)
		self.pipeM.setChannelSelected(1)
		self.setPrevSelected(1)
		self.setChannelSelected(1)

	# Callback function for the "Choose File" button
	def choose_file(self):
		# Good old Qt makes an open dialog window for us in one line...
		filepath = QFileDialog.getOpenFileName(self, 'Choose File')

		if filepath:
			self.pipeM.addVideoPlayback(filepath)

	# Centers the application window in the middle of the screen
	def center(self):
		screen = QtGui.QDesktopWidget().screenGeometry()
		size =  self.geometry()
		self.move((screen.width()-size.width())/2, ((screen.height()-size.height())/2)-50)

	# Used to watch for keyboard presses of 1-9 and Q-Y. These are used to change the selected channel
	# both through the Pipeline Manager and display the selection visually in the GUI
	def keyPressEvent(self, event):
		if event.key() == QtCore.Qt.Key_1:
			self.pipeM.setChannelSelected(1)
			self.setChannelSelected(1)

		elif event.key() == QtCore.Qt.Key_2:
			self.pipeM.setChannelSelected(2)
			self.setChannelSelected(2)

		elif event.key() == QtCore.Qt.Key_3:
			self.pipeM.setChannelSelected(3)
			self.setChannelSelected(3)

		elif event.key() == QtCore.Qt.Key_4:
			self.pipeM.setChannelSelected(4)
			self.setChannelSelected(4)

		elif event.key() == QtCore.Qt.Key_5:
			self.pipeM.setChannelSelected(5)
			self.setChannelSelected(5)

		elif event.key() == QtCore.Qt.Key_6:
			self.pipeM.setChannelSelected(6)
			self.setChannelSelected(6)

		elif event.key() == QtCore.Qt.Key_Q:
			self.pipeM.setPrevSelected(1)
			self.setPrevSelected(1)

		elif event.key() == QtCore.Qt.Key_W:
			self.pipeM.setPrevSelected(2)
			self.setPrevSelected(2)

		elif event.key() == QtCore.Qt.Key_E:
			self.pipeM.setPrevSelected(3)
			self.setPrevSelected(3)

		elif event.key() == QtCore.Qt.Key_R:
			self.pipeM.setPrevSelected(4)
			self.setPrevSelected(4)

		elif event.key() == QtCore.Qt.Key_T:
			self.pipeM.setPrevSelected(5)
			self.setPrevSelected(5)

		elif event.key() == QtCore.Qt.Key_Y:
			self.pipeM.setPrevSelected(6)
			self.setPrevSelected(6)

		elif event.key() == QtCore.Qt.Key_Escape:
			self.close()


	def setupVideoWidgets(self):
		# Setup Qt widgets for video overlay. Puts them in arrays so they can be easily accessed
		# for the channels
		videoWidgets = [ self.uim.prodPrevWidget1, self.uim.prodPrevWidget2, 
								self.uim.prodPrevWidget3, self.uim.prodPrevWidget4, 
								self.uim.prodPrevWidget5, self.uim.prodPrevWidget6, 
								self.uim.prodVideoWidget, self.uim.prodVideoWidget2 ]

		videoBorders = [ self.uim.prodPrevBorder1, self.uim.prodPrevBorder2, 
								self.uim.prodPrevBorder3, self.uim.prodPrevBorder4, 
								self.uim.prodPrevBorder5, self.uim.prodPrevBorder6 ]

		# Make sure widgets are configured properly for video overlay. You can try without these
		# to see what happens. Basically sets the widgets for optimum video overlay so they don't 
		# flicker when resizing the windows etc.
		for videoWidget in videoWidgets:
			videoWidget.setAttribute(0, 1) # AA_ImmediateWidgetCreation == 0
			videoWidget.setAttribute(QtCore.Qt.WA_NativeWindow) # WA_NativeWindow == 3
			videoWidget.setAttribute(QtCore.Qt.WA_PaintOnScreen) # WA_NoSystemBackground
			videoWidget.setAttribute(QtCore.Qt.WA_OpaquePaintEvent)

		# Sets last selected channel to the number of channels (therefore last channel) for initialisation
		self.lastmix1chan = num_channels
		self.lastmix2chan = num_channels

		return (videoWidgets, videoBorders)

	# Method to change the colour of the borders around the video preview widgets to show
	# which channel is selected for output
	def setChannelSelected(self, channel):
		if channel != self.lastmix1chan:
			self.videoBorders[channel - 1].setStyleSheet("background-color: #00ff00;")
			if self.lastmix1chan == self.lastmix2chan:
				# note this is why we put the widgets in arrays - so we can access them per channel.
				self.videoBorders[self.lastmix1chan - 1].setStyleSheet("background-color: #00deff;")
			else:
				self.videoBorders[self.lastmix1chan - 1].setStyleSheet("background-color: #292929;")
		
		self.lastmix1chan = channel

	# Method to change the colour of the borders around the video preview widgets to show
	# which channel is selected for preview
	def setPrevSelected(self, channel):
		if channel != self.lastmix2chan:
			self.videoBorders[channel - 1].setStyleSheet("background-color: #00deff;")
			if self.lastmix1chan == self.lastmix2chan:
				self.videoBorders[self.lastmix2chan - 1].setStyleSheet("background-color: #00ff00;")
			else:
				self.videoBorders[self.lastmix2chan - 1].setStyleSheet("background-color: #292929;")

		self.lastmix2chan = channel


	# Used to gracefully shutdown the GStreamer Pipeline on exit. Stops a bunch of nasty X Server Errors
	def closeEvent(self, event):
		self.pipeM.pipeline.set_state(gst.STATE_NULL)
		gst.element_state_get_name(gst.STATE_NULL)


#### PIPELINE MANAGER CLASS ####
class PipelineManager(QtGui.QMainWindow):

	# Method to create the initial pipeline (see the first diagram in the forum post)
	def createPipeline(self, userinterface, videoWidgets, videoBorders):

		self.ui = userinterface
		self.videoWidgets = videoWidgets
		self.videoBorders = videoBorders

		# Creates our GStreamer pipeline
		self.pipeline = gst.Pipeline("pipeline")

		# Create main elements
		videobars = gst.element_factory_make('videotestsrc', 'videobars')
		videotee = gst.element_factory_make('tee', 'videotee')

		# Sets the video test source to the height, width and framerate specified in the global vars
		videocaps = gst.Caps('video/x-raw-yuv, width=%d, height=%d, framerate=%d/1' % (video_width, video_height, video_framerate) )

		videoqueue1 = gst.element_factory_make('queue', 'videoqueue1')
		videoqueue2 = gst.element_factory_make('queue', 'videoqueue2')

		colorspace1 = gst.element_factory_make('ffmpegcolorspace', 'colorspace1')
		colorspace2 = gst.element_factory_make('ffmpegcolorspace', 'colorspace2')

		self.videomixer1 = gst.element_factory_make('videomixer', 'videomixer1')
		self.videomixer2 = gst.element_factory_make('videomixer', 'videomixer2')

		colorspace3 = gst.element_factory_make('ffmpegcolorspace', 'colorspace3')
		colorspace4 = gst.element_factory_make('ffmpegcolorspace', 'colorspace4')

		videooutput1 = gst.element_factory_make('autovideosink', 'videooutput1')
		videooutput2 = gst.element_factory_make('autovideosink', 'videooutput2')

		# Add the elements to the pipeline
		self.pipeline.add(videobars, videotee, videoqueue1, videoqueue2,
					colorspace1, colorspace2, self.videomixer1, self.videomixer2, 
					colorspace3, colorspace4, videooutput1, videooutput2)

		# Link these elements together
		videobars.link(videotee, videocaps)
		gst.element_link_many(videotee, videoqueue1, colorspace1)
		gst.element_link_many(videotee, videoqueue2, colorspace2)

		# Request the videomixer pads
		mixer1_driver_pad = self.videomixer1.get_request_pad("sink_%d" % max_num_channels)
		mixer2_driver_pad = self.videomixer2.get_request_pad("sink_%d" % max_num_channels)

		# Link the colorspace and mixer pads together
		cspace_pad = colorspace1.get_pad("src")
		cspace_pad.link(mixer1_driver_pad)

		cspace_pad = colorspace2.get_pad("src")
		cspace_pad.link(mixer2_driver_pad)

		# Link the videomixers to the output colorspace and videosinks
		gst.element_link_many(self.videomixer1, colorspace3, videooutput1)
		gst.element_link_many(self.videomixer2, colorspace4, videooutput2)

		# Setup video prview queues and video sinks
		self.videoSinks = []
		self.videoQueues = []
		self.mixer1Pads = []
		self.mixer2Pads = []

		# Loop through to create the video channel outputs and link them to the video test source tee
		for i in range(0,num_channels):
			self.videoSinks.append(gst.element_factory_make('autovideosink', 'prevsink_%d' % i))
			self.videoQueues.append(gst.element_factory_make('queue', 'prevqueue_%d' % i))
			self.mixer1Pads.append(mixer1_driver_pad)
			self.mixer2Pads.append(mixer2_driver_pad)
			self.pipeline.add(self.videoSinks[i], self.videoQueues[i])

			gst.element_link_many(videotee, self.videoQueues[i], self.videoSinks[i])

		# Create bus watches - used to watch for when the video sinks are ready to have video overlaid
		self.bus = self.pipeline.get_bus()
		self.bus.add_signal_watch()
		self.bus.enable_sync_message_emission()
		self.bus.connect('message', self.on_message)
		self.bus.connect("sync-message::element", self.on_sync_message)

		self.lastmix1chan = num_channels
		self.lastmix2chan = num_channels

		self.selChan = 1

	# Method to add a video player to the pipeline (see the second diagram in the forum post)
	def addVideoPlayback(self, source):
		# Create the bin for these elements to be created in
		player = gst.Bin("vidPlayer_%d" % self.selChan)

		# Create the elements
		plsource = gst.element_factory_make('filesrc')
		pldec = gst.element_factory_make('decodebin')
		pltee = gst.element_factory_make("tee")
		plqueue1 = gst.element_factory_make("queue")
		plqueue2 = gst.element_factory_make("queue")
		plqueue3 = gst.element_factory_make("queue")
		plcolorspace1 = gst.element_factory_make("ffmpegcolorspace")
		plcolorspace2 = gst.element_factory_make("ffmpegcolorspace")
		plcolorspace3 = gst.element_factory_make("ffmpegcolorspace")

		plaudioconvert = gst.element_factory_make("audioconvert")
		plaudiosink = gst.element_factory_make("autoaudiosink")

		# Add the elements to the bin
		player.add(plsource, pldec, pltee, plqueue1, plqueue2, plqueue3,
							plaudioconvert, plaudiosink, plcolorspace1,
							plcolorspace2, plcolorspace3)

		# Link the elements together
		plsource.link(pldec)

		gst.element_link_many(pltee, plqueue1, plcolorspace1)
		gst.element_link_many(pltee, plqueue2, plcolorspace2)
		gst.element_link_many(pltee, plqueue3, plcolorspace3)

		# Video decoding needs to be dynamically linked at runtime - it is only then it know what type
		# of media it needs to decode. To do this you specify a 'new-decoded-pad' and the callback for when
		# this happens.
		self.vpad = pltee.get_pad('sink')
		self.apad = plaudioconvert.get_pad('sink')
		pldec.connect('new-decoded-pad', self.on_new_decoded_pad)

		# Set the location of the video to play
		plsource.set_property('location', source)

		# This creates the 'ghost pads' for vidPlayer bin. This allows to connect the bin to other elements
		binsink1 = gst.GhostPad("src_1", plcolorspace1.get_pad("src"))
		binsink2 = gst.GhostPad("src_2", plcolorspace2.get_pad("src"))
		binsink3 = gst.GhostPad("src_3", plcolorspace3.get_pad("src"))
		player.add_pad(binsink1)
		player.add_pad(binsink2)
		player.add_pad(binsink3)

		# For now I'm connecting to a fakesink (black hole!) as I can't manage to get it to 
		# connect to the videosink correctly
		plfakesink1 = gst.element_factory_make("fakesink")

		# Set the bin to playing
		player.set_state(gst.STATE_PLAYING)
		plfakesink1.set_state(gst.STATE_PLAYING)
		gst.element_state_get_name(gst.STATE_PLAYING)

		self.connectChannel(self.selChan, player, self.videoSinks[self.selChan - 1])
		#self.counter = self.counter - 1

	# Method to connect the newly created bin into the existing pipeline on the channel specified
	def connectChannel(self, channel, bin, fakesink):
		pad0 = self.videoQueues[channel - 1].get_pad("src")
		pad1 = bin.get_pad("src_1")
		pad2 = bin.get_pad("src_2")
		pad3 = bin.get_pad("src_3")


		# Block the pads to stop segments escaping from them (to cleanly connect to the existing pipeline)
		pad2.set_blocked(True)
		pad3.set_blocked(True)
		pad0.set_blocked(True)

		# Add the bin and fakesink to the pipeline
		self.pipeline.add(bin)
		self.videoQueues[channel - 1].unlink(self.videoSinks[channel - 1])
		#self.videoQueues[channel - 1].get_pad("src").unlink(fakesink.get_pad("sink"))
		bin.link_pads("src_1", fakesink, "sink")

		# Get a new pad from the videomixers to connect the bin into
		self.mixer1Pads[channel - 1] = self.videomixer1.get_request_pad('sink_%d' % (channel))
		self.mixer2Pads[channel - 1] = self.videomixer2.get_request_pad('sink_%d' % (channel))

		# Set the Z-order of the videomixer channels. This is a bit dodgy at the moment!
		if self.lastmix1chan == channel:
			self.mixer1Pads[channel - 1].set_property('zorder', (max_num_channels + 1))
		else:
			self.mixer1Pads[channel - 1].set_property('zorder', 1)

		if self.lastmix2chan == channel:
			self.mixer2Pads[channel - 1].set_property('zorder', (max_num_channels + 1))
		else:
			self.mixer2Pads[channel - 1].set_property('zorder', 1)

		# Link to the videomixer
		pad2.link(self.mixer1Pads[channel - 1])
		pad3.link(self.mixer2Pads[channel - 1])

		# Unblock the pads
		pad2.set_blocked(False)
		pad3.set_blocked(False)

		# Now to connect to the video preview screens - Firstly I want to remove the queue connected to the 
		# video preview channel but that doesn't seem to be workin so instead I'm just creating a 
		# fakesink to link it to that instead
		#qfakesink = gst.element_factory_make("fakesink")
		#qfakesink.set_state(gst.STATE_PLAYING)
		#self.pipeline.add(qfakesink)

		

		#self.videoQueues[channel - 1].unlink(self.videoSinks[channel - 1])
		#self.videoQueues[channel - 1].link(qfakesink)

		# Now I want to link the bin with the videosink instead of its 
		# fakesink...but I really can't get it to work without freezing up!! Instead I'll pause it :(
		#self.videoSinks[channel - 1].set_state(gst.STATE_PAUSED)
		#gst.element_state_get_name(gst.STATE_PAUSED)

		pad0.set_blocked(False)


	# Method to disconnect a connected bin
	def disconnectChannel(self, channel, bin):
		print 'Yep...haven\'t done this yet'

	# Method to set the selected video channel to be at the front of the output videomixer
	def setChannelSelected(self, channel):
		if channel != self.lastmix1chan:
			self.mixer1Pads[self.lastmix1chan - 1].set_property('zorder', 1)
			self.mixer1Pads[channel - 1].set_property('zorder', (max_num_channels + 1))
			self.selChan=channel

			self.lastmix1chan = channel

	# Method to set the selected video channel to be at the front of the preview videomixer
	def setPrevSelected(self, channel):
		if channel != self.lastmix2chan:
			self.mixer2Pads[self.lastmix2chan - 1].set_property('zorder', 1)
			self.mixer2Pads[channel - 1].set_property('zorder', (max_num_channels + 1))

			self.lastmix2chan = channel

	# Method called to connect the decodebin when the video and audio has been linked in
	def on_new_decoded_pad(self, element, pad, last):
		caps = pad.get_caps()
		name = caps[0].get_name()
		if name == 'video/x-raw-rgb':
			if not self.vpad.is_linked(): # Only link once
				pad.link(self.vpad)
		elif name == 'audio/x-raw-int':
			if not self.apad.is_linked():
				pad.link(self.apad)


	def on_message(self, bus, message):
		t = message.type
		if t == gst.MESSAGE_EOS:
			player.set_state(gst.STATE_NULL)
		elif t == gst.MESSAGE_ERROR:
			player.set_state(gst.STATE_NULL)
			err, debug = message.parse_error()
			print 'Error: %s' % err, debug

	# Method used to check for 'prepare-xwindow-id' messages on the bus. These are posted when the
	# video sinks are ready to be overlaid onto the corresponding GUI widgets
	def on_sync_message(self, bus, message):
		if message.structure is None:
			return
		message_name = message.structure.get_name()
		if message_name == "prepare-xwindow-id":

			# Check which video sink they are from and get the correct window Id of that widget
			if message.src.get_name().find('videooutput1') > -1 :
				win_id = self.ui.prodVideoWidget2.winId()
			elif message.src.get_name().find('videooutput2') > -1 :
				win_id = self.ui.prodVideoWidget.winId()
			# If they are one of the preview sinks get the number from the 9th digit of the name. This
			# obviously only works if we have less than 10 channels!
			else:
				sink_id = message.src.get_name()[9:10]
				if sink_id.isdigit():
					win_id = self.videoWidgets[int(sink_id)].winId()
				else:
					return

			assert win_id

			device = message.src

			# Mac gets annoyed if you try and set to force and aspect ratio. Windows just does nothing.
			# Linux is good :)
			if platform.system() != 'Darwin':
				device.set_property("force-aspect-ratio", True)

			device.set_xwindow_id(int(win_id)) # Note the integer casting - needed to make it work on Windows!


	def log(self, message):
		print message

# Main Program
if __name__ == "__main__":
	gobject.threads_init()
	app = QApplication(sys.argv)
	app.connect(app, SIGNAL('lastWindowClosed()'),
				app, SLOT('quit()'))

	# Load the main app class
	myapp = MainApp()
	myapp.center()
	myapp.show()

	# Set the pipeline to playing
	myapp.pipeM.pipeline.set_state(gst.STATE_PLAYING)

	sys.exit(app.exec_())

