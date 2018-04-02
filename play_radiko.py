#!/usr/bin/env python
# coding:utf-8
# vim: expandtab nowrap ts=2 sw=2 sts=2


from radiko import Radiko
import argparse
import datetime
import subprocess

from RadikoHLS import RadikoHLS

## for debugging
# import IPython
# import pprint
# pp = pprint.PrettyPrinter(indent=4)
# pprint = pp.pprint

def main():

  ## TODO:サブコマンドを使いたい
  parser = argparse.ArgumentParser(description='radiko の再生と録音を行いますよ')

  parser.add_argument('channel_name', help='チャンネル' )
  parser.add_argument('-d', '--duration',default='1800' , help='再生（録音）時間', type=int)
  parser.add_argument('-o', '--output'  , help='保存先',nargs='?', default=None,const='')
  parser.add_argument('--no-play-live',action='store_const',default=False,const=True, help='再生しない')
  parser.add_argument('--ft', help='開始日時分秒')
  parser.add_argument('--to', help='終了日時分秒')
  
  
  args = parser.parse_args()
  channel  = vars(args)['channel_name'].upper()
  duration = vars(args)['duration']
  ft = vars(args)['ft']
  to = vars(args)['to']
  #
  #radiko = Radiko()
  radiko = RadikoHLS()


  ##
  if vars(args)['ft'] != None :
    print('timeshift...')
    f_out = vars(args)['output']
    radiko.save_radiko_timefree(channel, ft, to, output=f_out)
    exit()

  ## 
  if vars(args)['no_play_live'] == True :
    print('only save ')
    f_out = vars(args)['output']
    radiko.save_radiko(channel,duration,output=f_out)
    exit()
  ##
  if vars(args)['output'] != None :
    print('live and save ')
    radiko.play_and_save_radiko(channel,duration, output=vars(args)['output'])
    exit()
  else:
    print('only -live')
    radiko.play_radiko(channel,duration)
    exit()



if __name__ == '__main__':
    main()


