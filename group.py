from task import Task
from PyQt5 import QtWidgets, QtCore

class Group(QtWidgets.QWidget):

	list_tasks = []

	def __init__(self,str_group_name, parent):
		QtWidgets.QWidget.__init__(self, parent, QtCore.Qt.Window)
		self.setWindowTitle(str_group_name)
		self.box_main = QtWidgets.QVBoxLayout()
		self.setLayout(self.box_main)
		self.create_task_panel()
		self.create_buttons()
		self.str_group_name = str_group_name
		self.parent = parent

	def add_task(
			self,
			str_task_name,
			str_task_string,
			int_task_value,
			int_task_result,
			bool_task_is_finished):
		self.list_tasks.append(
			Task(
				str_task_name,
				str_task_string,
				int_task_value,
				int_task_result,
				bool_task_is_finished
			)
		)
		self.box_task.addLayout(
			self.list_tasks[len(self.list_tasks) - 1].get_box())

	
	def create_task_panel(self):
		self.box_task = QtWidgets.QVBoxLayout()
		self.box_main.addLayout(self.box_task)

	def create_buttons(self):
		self.but_finished = QtWidgets.QPushButton("Finished tasks")
		self.but_finished.clicked.connect(self.func_finished)

		self.but_exit = QtWidgets.QPushButton("Exit")
		self.but_exit.clicked.connect(self.func_exit)

		self.but_save = QtWidgets.QPushButton("Save")
		self.but_save.clicked.connect(self.func_save)

		box_buttons = QtWidgets.QHBoxLayout()
		box_buttons.addWidget(self.but_finished)
		box_buttons.addWidget(self.but_save)
		box_buttons.addWidget(self.but_exit)

		self.box_main.addLayout(box_buttons)

	def func_finished(self):
		"""Modal window"""
		pass

	def func_exit():
		"""hide not delete"""
		self.func_save(self)
		pass

	def func_save(self):
		""" 
			key - name,
			0 - describe
			1 - main_rez
			2 - current_rez
		"""
		group_adress = self.parent.dict_tasks[self.str_group_name]
		for task in self.list_tasks:
			task_adress = group_adress[task.get_name()]
			task_adress[2] = task.get_current_result()

