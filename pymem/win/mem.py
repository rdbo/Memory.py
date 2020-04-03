import win32api
import win32process
import win32con
import win32ui
import win32gui
import psutil
import ctypes
from ctypes import *

kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)

#Functions
from win32api import OpenProcess
from win32api import GetCurrentProcessId
from win32api import GetModuleHandle
from win32process import GetWindowThreadProcessId
ReadProcessMemory=windll.kernel32.ReadProcessMemory
WriteProcessMemory=windll.kernel32.WriteProcessMemory

#Constants
from win32con import PROCESS_ALL_ACCESS
NULL=0
INVALID_PID=-1
BAD_RETURN=NULL

#Memory

class Memory:
	def GetProcessIdByName(strProcessName):
		for process in psutil.process_iter():
			if(process.name() == strProcessName):
				return process.pid
		return INVALID_PID

	def GetProcessIdByWindow(strWindowName, strWindowClass=None):
		return GetWindowThreadProcessId(win32ui.FindWindow(strWindowClass, strWindowName).GetSafeHwnd())[1]

	def GetProcessHandle(pid):
		return OpenProcess(PROCESS_ALL_ACCESS, NULL, pid)

	def GetCurrentProcessID():
		return GetCurrentProcessId()

	def WriteBuffer(hProcess, address, value, size):
		WriteProcessMemory(hProcess, address, value, size, NULL)

	def ReadBuffer(hProcess, address, pBuffer, size):
		ReadProcessMemory(hProcess, address, pBuffer, size)

	def IsProcessRunning(pid):
		return psutils.pid_exists(pid)