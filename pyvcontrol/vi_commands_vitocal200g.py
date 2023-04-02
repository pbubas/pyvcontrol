ACCESS_MODE = 'access_mode'
UNIT = 'unit'
LENGTH = 'length'
ADDRESS = 'address'

VITOCAL200G = {
    # Commands for Vitocal 200-G

    'TempZew': {ADDRESS: '0101', LENGTH: 2, UNIT: 'IS10'},

    'CwuTemp': {ADDRESS: '010d', LENGTH: 2, UNIT: 'IS10'},

    'BuforTemp': {ADDRESS: '010b', LENGTH: 2, UNIT: 'IS10'},

    'CoTempZasilanie': {ADDRESS: '0114', LENGTH: 2, UNIT: 'IS10'},

    'TempGlikolWejscie': {ADDRESS: '0103', LENGTH: 2, UNIT: 'IS10'},

    'WtornyTempZasilanie': {ADDRESS: '0105', LENGTH: 2, UNIT: 'IS10'},

    'WtornyTempPowrot': {ADDRESS: '0106', LENGTH: 2, UNIT: 'IS10'},

    'PompaWtornaMoc%': {ADDRESS: 'B421', LENGTH: 2, UNIT: 'IUNON'},

    'CwuTempZadana': {ADDRESS: '6000', LENGTH: 2, UNIT: 'IS10', ACCESS_MODE: 'write', 'min_value': 10,
                           'max_value': 60},

    'Sprezarka' : {ADDRESS: '5000', LENGTH: 2, UNIT: 'IUNON', ACCESS_MODE: 'write', 'min_value': 0, 'max_value': 1}

    #'BilansEnergetycznyCzynnika': {ADDRESS: '163F', LENGTH: 1, UNIT: 'IUNON'},
}