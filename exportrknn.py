from rknn.api import RKNN
import argparse
from os import path

def convertONNXtoRKNN(
        ONNX_path,
        RKNN_path = None,
        optimization = 0,
        target_platform = 'rk3588',
        quantization = False,
        verbose = False
    ):
    rknn = RKNN(verbose = verbose)

    #Pre-process config
    print("--> Beginning Pre-Process Configuration")
    rknn.config(target_platform = target_platform, optimization_level = optimization)
    print("Pre-Process Configuration Complete")

    print("--> Loading ONNX Model")
    ret = rknn.load_onnx(ONNX_path)
    if ret != 0:
        print("failed to load ONNX Model at " + ONNX_path)
        exit(ret)

    print('--> Building model')
    ret = rknn.build(do_quantization=quantization)
    if ret != 0:
        print('Build model failed!')
        exit(ret)
    print('Building model done')

    # Export RKNN model
    print('--> Export rknn model')
    ret = rknn.export_rknn(RKNN_path)
    if ret != 0:
        print('Export rknn model failed!')
        exit(ret)
    print('Export rknn model done')

    rknn.release()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o","--onnx",type=str,help="Path to ONNX file to load from")
    parser.add_argument("-r","--rknn",type=str,help="Path to RKNN file to export to")
    parser.add_argument("-t","--target",type=str,help="Platform to target")
    parser.add_argument("--optimize",type=int,default=0,nargs='?',const=10,help="How much to optimize the model, between 0 and 10")
    parser.add_argument("-v","--verbose",action="store_true",help="Enables verbose mode")
    parser.add_argument("-q","--quantize",action="store_true",help="Enables quantization")

    args = parser.parse_args()

    convertONNXtoRKNN(args.onnx,args.rknn,args.optimize,args.target,args.quantize,args.verbose)
