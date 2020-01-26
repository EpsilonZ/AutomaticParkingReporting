import os
import json

class Config:

	def __init__(self, pathToConfigFile):
		self.json_config = self.load_config_file(pathToConfigFile)

	def load_config_file(self, pathToConfigFile):
		json_config = {}
		with open(pathToConfigFile) as configFile:
			json_config = json.load(configFile)
		return json_config

	def get_config_info_by_key(key):

		try:
			return self.json_config[key]
		except:
			return 0

	def get_bboxes_config_file_path(self):

		return self.json_config['street_bboxes']

	def config_file_info(self):
		return str(self.json_config)

