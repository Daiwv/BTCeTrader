#!/usr/bin/python
# -*- coding: utf-8 -*-
###################################################################################################
import sys, json, time, os

from threading import Timer
from random import randint
from sys import stdout
from time import sleep

###################################################################################################
class Sound(object):
    
    # =======================================================================
    def __init__(self, parent=None):

        # -------------------------------------------------------------------
        self.AVAILABLE                          = False;
        self.PARENT                             = parent;

        self.PLAYER                             = " mpg123 ";
        self.PLAYER_PARAMS                      = " -q ";
        self.SS_PATH                            = "./data/sound/";
        self.SS                                 = [ 
                                                    "notification-1.mp3",
                                                    "notification-2.mp3",
                                                    "notification-3.mp3",
                                                    "error.mp3",
                                                    "beep.mp3",
                                                ];
        # -------------------------------------------------------------------
        self.INIT();
        # -------------------------------------------------------------------

    # =======================================================================
    def INIT(self):

        # -------------------------------------------------------------------
        #self.RING( _type=1 );

        self.AVAILABLE = True;
        # -------------------------------------------------------------------

    # =======================================================================
    def RING(self, _type):

        # -------------------------------------------------------------------
        try:

            B_TIMER = Timer(0.05, self.MAKE_RING, [_type] );
            B_TIMER.start();

        except Exception as _exception:
            self.PARENT.LOG["error"].append(" Sound: <br/>"+str(_exception));
        # -------------------------------------------------------------------

    # =======================================================================
    def MAKE_RING(self, _type):

        # -------------------------------------------------------------------
        try:
            os.system( self.PLAYER + self.PLAYER_PARAMS + self.SS_PATH + self.SS[_type]+" ");

        except Exception as _exception:
            self.PARENT.LOG["error"].append(" Sound: <br/>"+str(_exception));
        # -------------------------------------------------------------------

    # =======================================================================
    def SOUND_TEST(self):

        # -------------------------------------------------------------------
        self.RING( _type=0 ); sleep(1);
        self.RING( _type=1 ); sleep(1);
        self.RING( _type=2 ); sleep(1);
        self.RING( _type=3 ); sleep(1);
        self.RING( _type=4 );

        # -------------------------------------------------------------------

    # =======================================================================

###################################################################################################
