import os as _os
import logging
from subprocess import Popen, PIPE


def getFiles(path, allowed=None):
	"""	provieds files for provided path

		Arguments:
			path(str) : path where to look for files
			allowed(list) : list of filetype 
			format to exclude files.
	"""

	allowed = allowed or ['.jpg']
	allFiles = []
	filesAndFolders = _os.listdir(path)
	for item in filesAndFolders:
		# print item, _os.path.splitext(item)[-1]
		_file = _os.path.join(path, item)
		if _os.path.isfile(_file) and _os.path.splitext(_file)[-1] in allowed:
			allFiles.append(_file)

	return allFiles

def validateFilePathExists(filePath):
	return _os.path.exists(filePath)


def _buildTasks(filePaths, toPath, processType='cp', args=''):
	if not validateFilePathExists(toPath):
		# copy to or move to path doesnt exists
		return None

	tasks = []
	for filePath in filePaths:
		if not validateFilePathExists(filePath):
			# skipping copying filePath as it doesnt exist on disk
			continue
		tasks.append([processType, args, filePath, toPath])

	return tasks


def executeTasks(tasks):
	print "{0} tasks to perform.".format(len(tasks))
	for task in tasks:
		process = Popen(task, stdout=PIPE, stderr=PIPE)
		stdout, stderr = process.communicate()
		print stdout, stderr

tasks = _buildTasks(getFiles('/Users/sanjeevkumar/Desktop'), '/Users/sanjeevkumar/Pictures/delete/', processType='mv')

executeTasks(tasks)

