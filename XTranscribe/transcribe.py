from basic_pitch.inference import predict_and_save

from .common import bcolors
from .speech_enhance import noise_reduction

PROC_NAME = f'{bcolors.BOLD}[XTRANSCRIBE]{bcolors.ENDC}'

def transcribe(wav_path, output_directory='temporary', denoise=False):
    if denoise:
        print(PROC_NAME, 'Denoising input:', wav_path)
        wav_path_no_noise = output_directory+'/'+(''.join(wav_path.split('.')[:-1]) +'_no_noise.wav').split('/')[-1]
        noise_reduction(wav_path, wav_path_no_noise)
        print(PROC_NAME, 'Denoised:', wav_path_no_noise)
    else:
        wav_path_no_noise = wav_path
    print(PROC_NAME, 'Transcribing:', wav_path_no_noise)
    predict_and_save(
        [wav_path_no_noise], # predict takes in a list of path
        output_directory=output_directory,
        save_midi=True,
        sonify_midi=False, # 很糟糕的 to wav 
        save_model_outputs=False, # npz
        save_notes=False # csv
    )
    midi_path = output_directory+'/'+(''.join(wav_path_no_noise.split('.')[:-1]) +'_basic_pitch.mid').split('/')[-1]
    print(PROC_NAME, 'Transcribed:', midi_path)
    return midi_path


def transcribe_csv(wav_path, output_directory='temporary', denoise=False):
    if denoise:
        print(PROC_NAME, 'Denoising input:', wav_path)
        wav_path_no_noise = output_directory+'/'+(''.join(wav_path.split('.')[:-1]) +'_no_noise.wav').split('/')[-1]
        noise_reduction(wav_path, wav_path_no_noise)
        print(PROC_NAME, 'Denoised:', wav_path_no_noise)
    else:
        wav_path_no_noise = wav_path
    print(PROC_NAME, 'Transcribing:', wav_path_no_noise)
    predict_and_save(
        [wav_path_no_noise], # predict takes in a list of path
        output_directory=output_directory,
        save_midi=True,
        sonify_midi=False, # 很糟糕的 to wav 
        save_model_outputs=False, # npz
        save_notes=True # csv
    )
    midi_path = output_directory+'/'+(''.join(wav_path_no_noise.split('.')[:-1]) +'_basic_pitch.mid').split('/')[-1]
    csv_path = output_directory+'/'+(''.join(wav_path_no_noise.split('.')[:-1]) +'_basic_pitch.csv').split('/')[-1]
    print(PROC_NAME, 'Transcribed:', (midi_path, csv_path))
    return midi_path, csv_path