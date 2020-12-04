from PyQt5 import QtWidgets, Qt

class Task():
	"""docstring for Task"""
	def __init__(
			self,
			str_task_name,
			str_task_string,
			int_task_value,
			int_task_result,
			bool_task_is_finished):
		self.box_line = QtWidgets.QHBoxLayout()

		self.label_name = QtWidgets.QLabel(str_task_name)
		self.label_name.setFrameStyle(Qt.QFrame.Box)

		self.label_describe = QtWidgets.QLabel(str_task_string)
		self.label_describe.setFrameStyle(Qt.QFrame.Box)

		self.label_progress = QtWidgets.QLabel(
			str(int_task_value) + "/" + str(int_task_result))
		self.label_progress.setFrameStyle(Qt.QFrame.Box)

		self.increment_widget = QtWidgets.QSpinBox();
		self.increment_widget.setValue(0)

		self.bool_task_is_finished = bool_task_is_finished

		self.box_line.addWidget(self.label_name)
		self.box_line.addWidget(self.label_describe)
		self.box_line.addWidget(self.label_progress)
		self.box_line.addWidget(self.increment_widget)

		self.int_task_result = int_task_result
		self.str_task_name = str_task_name

	def get_box(self):
		return self.box_line

	def get_name(self):
		return self.str_task_name 

	def get_current_result(self):
		return self.int_task_result + self.increment_widget.value()

	def is_finished(self):
		return self.bool_task_is_finished