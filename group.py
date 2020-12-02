from PyQt5 import QtWidgets, QtCore

class Group(QtWidgets.Qwidget):

	list_tasks = []

	def __init__(str_group_name, parent):
		QtWidgets.Qwidget.__init__(self, parent, QtCore.Qt.Window)
		self.setWindowTitle(str_group_name)
		self.box_main = QtWidgets.QVBoxLayout()
		self.setLayout(self.box_main)
		self.create_task_panel()
		self.create_buttons()

	def add_task(
			str_task_name,
			str_task_string,
			int_task_value,
			int_task_result,
			bool_task_is_finished):
		list_tasks.append[
			Task(
				str_task_name,
				str_task_string,
				int_task_value,
				int_task_result,
				bool_task_is_finished
			)
		]
		self.box_task.addWidget(
			list_tasks[len(list_tasks) - 1].getBox())

	
	def create_task_panel():
		self.box_task = QtWidgets.QVBoxLayout()
		self.box_main.addLayout(self.box_task)

	def create_buttons():
		self.but_finished = QtWidgets.QPushButton("Finished tasks")
		self.but_finished.clicked.connect(self.func_finished)

		self.but_exit = QtWidgets.QPushButton("Exit")
		self.but_exit = QtWidgets.QPushButton(self.func_exit)

		box_buttons = QtWidgets.QHBoxLayout()
		box_buttons.addWidget(but_finished)
		box_buttons.addWidget(but_exit)

		self.box_main.addLayout(box_buttons)

	def func_finished():
		"""Modal window"""
		pass

	def func_exit():
		"""hide not delete"""
		pass

	def get_tasks():
		pass