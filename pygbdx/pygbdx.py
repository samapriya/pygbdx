#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import os
import glob
import subprocess
from gbdx_validate import validate
from simplesearch import search
from gbdx_mexport import mxp
from gbdx_fpexport import fxp
os.chdir(os.path.dirname(os.path.realpath(__file__)))
path=os.path.dirname(os.path.realpath(__file__))


def init():
    subprocess.call('python authenticator.py', shell=True)
def init_from_parser(args):
    init()

def info_from_parser(args):
    validate()

def simple_search_from_parser(args):
    search(path=args.local,
              start=args.start,
              end=args.end,
              limit=int(args.limit))
def metadata_from_parser(args):
    mxp(path=args.local,
              start=args.start,
              end=args.end,
              limit=int(args.limit))

def footprint_from_parser(args):
    fxp(path=args.local,
              dir=args.dirc,
              output=args.output)

# def refresh():
#     filelist = glob.glob(os.path.join(path, "*.csv"))
#     for f in filelist:
#         os.remove(f)
#     subprocess.call('python ee_rep.py', shell=True)
#     subprocess.call('python gitcl.py', shell=True)



# def refresh_from_parser(args):
#     refresh()


# def idsearch_from_parser(args):
#     idsearch(mname=args.name)

# def intersect_from_parser(args):
#     intersect(start=args.start,
#               end=args.end,
#               geojson=args.aoi,
#               operator=args.operator,
#               output=args.report)

# def imgexp_from_parser(args):
#     imgexp(collection=args.id)


# def exp_from_parser(args):
#     exp(
#         collection=args.id,
#         folderpath=args.folder,
#         typ=args.type,
#         start=args.start,
#         end=args.end,
#         bandnames=args.bandlist,
#         geojson=args.aoi,
#         operator=args.operator,
#         )
spacing = '                               '

def main(args=None):
    parser = argparse.ArgumentParser(description='GBDX Simple CLI')

    subparsers = parser.add_subparsers()
    parser_init = subparsers.add_parser('init',help='Initialize GBDX')
    parser_init.set_defaults(func=init_from_parser)

    parser_info = subparsers.add_parser('info',help='Prints account info for GBDX')
    parser_info.set_defaults(func=info_from_parser)

    parser_simple_search = subparsers.add_parser('simple_search',help='Simple search to look for DG assets that intersect your AOI handles KML/SHP/GEOJSON')
    parser_simple_search.add_argument('--local',help='full path for folder or file with SHP/KML/GEOJSON')
    parser_simple_search.add_argument('--start',help='start date YYYY-MM-DD')
    parser_simple_search.add_argument('--end',help='end date YYYY-MM-DD')
    parser_simple_search.add_argument('--limit',help='Limit the number of items to search')
    parser_simple_search.set_defaults(func=simple_search_from_parser)

    parser_metadata = subparsers.add_parser('metadata',help='Exports metadata for simple search into constitutent folders as JSON files')
    parser_metadata.add_argument('--local',help='full path for folder or file with SHP/KML/GEOJSON')
    parser_metadata.add_argument('--start',help='start date YYYY-MM-DD')
    parser_metadata.add_argument('--end',help='end date YYYY-MM-DD')
    parser_metadata.add_argument('--limit',help='Limit the number of items to search')
    parser_metadata.set_defaults(func=metadata_from_parser)

    parser_footprint = subparsers.add_parser('footprint',help='Exports footprint for metadata files extracted earlier and converts them to individual geometries (GeoJSON) and combined geomtry (GeoJSON) file')
    parser_footprint.add_argument('--local',help='full path for folder with metadata JSON files')
    parser_footprint.add_argument('--dirc',help='directory to store individual geometries')
    parser_footprint.add_argument('--output',help='path to combined footprint geometry geojson')
    parser_footprint.set_defaults(func=footprint_from_parser)

    args = parser.parse_args()

    args.func(args)


if __name__ == '__main__':
    main()
