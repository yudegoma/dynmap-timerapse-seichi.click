import minecraft_dynmap_timemachine.dynmap as dynmap
import minecraft_dynmap_timemachine.time_machine as time_machine
import minecraft_dynmap_timemachine.projection as projection
import os
import datetime
import cv2
from utils import crop, pil_to_cv2
from make_gif import make_gif

base_url = "http://map-s1.minecraftserver.jp/"
world = "world_SW"
map_name = "flat"
center = [-128, 0, -128]
size = [2, 2]
zoom = 4


def timerapse_dynmap():
    dm = dynmap.DynMap(base_url)
    maps = dm.worlds[world].maps
    dm_map = maps[map_name]
    m_loc = projection.MinecraftLocation(center[0], center[1], center[2], dm_map.worldtomap)
    tm = time_machine.TimeMachine(dm)

    # 画像保存の設定
    now = datetime.datetime.now()
    img_dir = "{0:%Y%m%d}".format(now)
    if not os.path.exists(img_dir):
        os.mkdir(img_dir)
    dest = img_dir + '/dyn_{0:%Y%m%d_%H%M}.png'.format(now)

    img = tm.capture_single(dm_map, m_loc.to_tile_location(zoom), size)
    cv2.imwrite(dest, crop(pil_to_cv2(img)))

    make_gif(img_dir)

if __name__ == '__main__':
    timerapse_dynmap()
