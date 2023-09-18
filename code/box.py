def box():
    print('its a box')
import multiprocessing
from cube import cube_print
if __name__=="__main__":
    p1=multiprocessing.Process(target=box)
    p2=multiprocessing.Process(target=cube_print)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('task done')
