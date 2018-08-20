#appModules/donotdisturb.py
#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2018 NV Access Limited, Saran Prasad Ambikapathy
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

import appModuleHandler

# A placebo class to be invoked for programmatically determined applications that 
# are expected not be accessed by NVDA.
class AppModule(appModuleHandler.AppModule):

	sleepMode = True