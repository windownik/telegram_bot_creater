import create_handlers
from create_main_files import *
from create_keyboards import *
from create_states import *

if __name__ == '__main__':
    creat_main()
    creat_json()
    creat_dispatcher()
    creat_states()
    creat_init()
    creat_keyboards()
    create_handlers.creat_hendler()
