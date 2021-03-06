from __future__ import annotations

from core.commons import constants
from core.util.model.Logger import Logger


class SuperManager:
	NAME = 'SuperManager'
	_INSTANCE = None


	def __new__(cls, *args, **kwargs):
		if not isinstance(SuperManager._INSTANCE, SuperManager):
			SuperManager._INSTANCE = object.__new__(cls)

		return SuperManager._INSTANCE


	def __init__(self, mainClass):
		SuperManager._INSTANCE = self
		self._managers = dict()

		self.projectAlice = mainClass
		self.commons = None
		self.commonsManager = None
		self.configManager = None
		self.databaseManager = None
		self.threadManager = None
		self.mqttManager = None
		self.timeManager = None
		self.networkManager = None
		self.snipsServicesManager = None
		self.hotwordManager = None


	def onStart(self):
		commons = self._managers.pop('CommonsManager')
		commons.onStart()

		configManager = self._managers.pop('ConfigManager')
		configManager.onStart()

		databaseManager = self._managers.pop('DatabaseManager')
		databaseManager.onStart()

		snipsServicesManager = self._managers.pop('SnipsServicesManager')
		snipsServicesManager.onStart()

		networkManager = self._managers.pop('NetworkManager')
		networkManager.onStart()

		mqttManager = self._managers.pop('MqttManager')
		mqttManager.onStart()

		for manager in self._managers.values():
			if manager:
				manager.onStart()

		self._managers[commons.name] = commons
		self._managers[configManager.name] = configManager
		self._managers[databaseManager.name] = databaseManager
		self._managers[mqttManager.name] = mqttManager
		self._managers[snipsServicesManager.name] = snipsServicesManager
		self._managers[networkManager.name] = networkManager


	def onBooted(self):
		for manager in self._managers.values():
			if manager:
				manager.onBooted()


	@staticmethod
	def getInstance() -> SuperManager:
		return SuperManager._INSTANCE


	def initManagers(self):
		from core.commons.CommonsManager import CommonsManager
		from core.base.ConfigManager import ConfigManager
		from core.server.MqttManager import MqttManager
		from core.util.DatabaseManager import DatabaseManager
		from core.util.ThreadManager import ThreadManager
		from core.util.TimeManager import TimeManager
		from core.util.NetworkManager import NetworkManager
		from core.snips.SnipsServicesManager import SnipsServicesManager
		from core.util.HotwordManager import HotwordManager

		self.commonsManager = CommonsManager()
		self.commons = self.commonsManager
		self.configManager = ConfigManager()
		self.databaseManager = DatabaseManager()
		self.threadManager = ThreadManager()
		self.mqttManager = MqttManager()
		self.timeManager = TimeManager()
		self.networkManager = NetworkManager()
		self.snipsServicesManager = SnipsServicesManager()
		self.hotwordManager = HotwordManager()

		self._managers = {name[0].upper() + name[1:]: manager for name, manager in self.__dict__.items() if name.endswith('Manager')}


	def onStop(self):
		managerName = constants.UNKNOWN_MANAGER
		try:
			mqttManager = self._managers.pop('MqttManager', None)

			for managerName, manager in self._managers.items():
				manager.onStop()

			if mqttManager:
				mqttManager.onStop()

		except Exception as e:
			Logger().logError(f'Error while shutting down manager "{managerName}": {e}')


	def getManager(self, managerName: str):
		return self._managers.get(managerName, None)


	@property
	def managers(self) -> dict:
		return self._managers
