VERSION = '1.0.0-a1'
DEFAULT_SITE_ID = 'default'
DEFAULT = 'default'
DUMMY = 'dummy'
UNKNOWN = 'unknown'
UNKNOWN_MANAGER = 'unknownManager'
UNKNOWN_USER = 'unknownUser'

DATABASE_FILE = 'system/database/data.db'
GITHUB_URL = 'https://github.com/project-alice-assistant'
GITHUB_RAW_URL = 'https://raw.githubusercontent.com/project-alice-assistant'
GITHUB_API_URL = 'https://api.github.com/repos/project-alice-assistant'
GITHUB_REPOSITORY_ID = 250856660

TOPIC_ALICE_GREETING = 'projectalice/devices/greeting'
TOPIC_NEW_HOTWORD = 'projectalice/devices/alice/newHotword'
TOPIC_ALICE_CONNECTION_ACCEPTED = 'projectalice/devices/connectionAccepted'
TOPIC_ALICE_CONNECTION_REFUSED = 'projectalice/devices/connectionRefused'
TOPIC_DISCONNECTING = 'projectalice/devices/disconnection'
TOPIC_CORE_RECONNECTION = 'projectalice/devices/coreReconnection'
TOPIC_CORE_DISCONNECTION = 'projectalice/devices/coreDisconnection'
TOPIC_DEVICE_HEARTBEAT = 'projectalice/devices/heartbeat'
TOPIC_CORE_HEARTBEAT = 'projectalice/devices/coreHeartbeat'
TOPIC_DND = 'projectalice/devices/stopListen'
TOPIC_STOP_DND = 'projectalice/devices/startListen'
TOPIC_TOGGLE_DND = 'projectalice/devices/toggleListen'
TOPIC_HOTWORD_TOGGLE_ON = 'hermes/hotword/toggleOn'
TOPIC_HOTWORD_TOGGLE_OFF = 'hermes/hotword/toggleOff'
TOPIC_HOTWORD_DETECTED = 'hermes/hotword/default/detected'
TOPIC_PLAY_BYTES = 'hermes/audioServer/{}/playBytes/#'
TOPIC_ASR_START_LISTENING = 'hermes/asr/startListening'
TOPIC_ASR_STOP_LISTENING = 'hermes/asr/stopListening'
TOPIC_AUDIO_FRAME = 'hermes/audioServer/{}/audioFrame'
TOPIC_PLAY_BYTES_FINISHED = 'hermes/audioServer/{}/playFinished'
TOPIC_VAD_UP = 'hermes/voiceActivity/{}/vadUp'
TOPIC_VAD_DOWN = 'hermes/voiceActivity/{}/vadDown'

TOPIC_CLEAR_LEDS = 'hermes/leds/clear'
TOPIC_DND_LEDS = 'hermes/leds/doNotDisturb'

TOPIC_DEVICE_STATUS = 'projectalice/devices/status'

EVENT_FULL_MINUTE = 'fullMinute'
EVENT_FIVE_MINUTE = 'fiveMinute'
EVENT_QUARTER_HOUR = 'quarterHour'
EVENT_FULL_HOUR = 'fullHour'
EVENT_SKILL_UPDATED = 'skillUpdated'
EVENT_BOOTED = 'booted'
EVENT_HOTWORD_TOGGLE_ON = 'hotwordToggleOn'
EVENT_HOTWORD_TOGGLE_OFF = 'hotwordToggleOff'
EVENT_HOTWORD = 'hotword'
EVENT_WAKEWORD = 'wakeword'
EVENT_PLAY_BYTES = 'playBytes'
EVENT_PLAY_BYTES_FINISHED = 'playBytesFinished'
EVENT_AUDIO_FRAME = 'audioFrame'
EVENT_START_LISTENING = 'startListening'
EVENT_STOP_LISTENING = 'stopListening'
EVENT_DND_ON = 'dndOn'
EVENT_DND_OFF = 'dndOff'
