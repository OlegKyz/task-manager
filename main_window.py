import sys
from group import Group
from PyQt5 import QtWidgets, QtCore, QtGui, Qt

class MainWindow(QtWidgets.QWidget):

	str_task_file_path = "tasks.txt";
	str_main_window_name = "Task Manager 2.0"
	int_base_x = 500
	int_base_y = 300
	list_groups = [];
	
	def __init__(self, parent = None):
		QtWidgets.QWidget.__init__(self, parent)
		self.dict_tasks = {}
		self.setWindowTitle(self.str_main_window_name)
		self.create_buttons()
		self.read_groups()
		self.move(self.int_base_x, self.int_base_y)


	def read_groups(self):
		try:
			input_file = open(self.str_task_file_path)
		except OSError as exception:
			print(exception)
			raise(exception)
		str_group_name = input_file.readline()[:-1]
		#try:
		while str_group_name != "":
			if not str_group_name in self.dict_tasks:
				self.dict_tasks[str_group_name] = {}

			str_task_name = input_file.readline()[:-1]

			self.dict_tasks[str_group_name].update(
				[(str_task_name,[])])

			str_task_string = input_file.readline()[:-1]
			self.dict_tasks[str_group_name][str_task_name].append(str_task_string)

			int_task_value = int(input_file.readline())
			self.dict_tasks[str_group_name][str_task_name].append(int_task_value)
			#print(int_task_value)
			int_task_result = int(input_file.readline())
			#print(int_task_result)
			self.dict_tasks[str_group_name][str_task_name].append(int_task_result)

			bool_task_is_finished = int_task_result > int_task_value
			
			new_group = Group(str_group_name, self)
			new_group.add_task(
				str_task_name,
				str_task_string,
				int_task_value,
				int_task_result,
				bool_task_is_finished)
			self.list_groups.append(new_group)

			str_group_name = input_file.readline()[:-1]

		input_file.close()
		#except ... as exception:

	def create_buttons(self):
		self.but_new_group = QtWidgets.QPushButton("New group")
		self.but_new_group.clicked.connect(self.func_new_group)

		self.but_show_group = QtWidgets.QPushButton("Show group")
		self.but_show_group.clicked.connect(self.func_show_group)

		self.but_show_all_groups = QtWidgets.QPushButton("Show all groups")
		self.but_show_all_groups.clicked.connect(self.func_show_all_groups)
		
		#self.but_delete_group = QtWidgets.QPushButton("Delete group")
		#self.but_delete_group.clicked.connect(self.func_delete_group)

		self.but_exit = QtWidgets.QPushButton("Exit")
		self.but_exit.clicked.connect(self.func_exit)

		box_butttons = QtWidgets.QVBoxLayout()
		box_butttons.addWidget(self.but_new_group)
		box_butttons.addWidget(self.but_show_group)
		box_butttons.addWidget(self.but_show_all_groups)
		#box_butttons.addWidget(self.but_delete_group)
		box_butttons.addWidget(self.but_exit)

		self.setLayout(box_butttons)

	def func_new_group(self):
		pass

	def func_show_group(self):
		pass

	def func_show_all_groups(self):
		self.list_groups[0].show()

	def func_delete(self):
		pass

	def func_exit(self):
		try:
			output_file = open(self.str_task_file_path, 'w')
		except OSError as exception:
			print(exception)
			raise(exception)
		for group in self.dict_tasks:
			for task in self.dict_tasks[group]:
				output_file.write(group + '\n')
				output_file.write(task  + '\n')
				output_file.write(self.dict_tasks[group][task][0]  + '\n' )
				output_file.write(str(self.dict_tasks[group][task][1])  + '\n')
				output_file.write(str(self.dict_tasks[group][task][2])  + '\n')


if __name__ == "__main__":

	app = QtWidgets.QApplication(sys.argv)
	main_window = MainWindow()
	main_window.show()

	sys.exit(app.exec_())