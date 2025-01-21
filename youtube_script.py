import os
import json
from moviepy.editor import VideoFileClip
import subprocess

def generate_transcription_and_keywords(whisper_path, youtube_link, jobname, model_name, outpath):
    # Ensure the output directory exists
    os.makedirs(outpath, exist_ok=True)

    # Download the video
    video_path = f"{outpath}/{jobname}.mp4"
    get_vid_material(youtube_link, video_path)

    # Extract and convert audio to the required format
    audio_path = f"{outpath}/{jobname}.wav"
    subprocess.run(f"ffmpeg -i {video_path} -af anull -ar 16000 -ac 1 -c:a pcm_s16le {audio_path}", shell=True)

    # Transcribe the audio to text
    transcription_path = f"{outpath}/{jobname}_transcription.vtt"
    subprocess.run(f"{whisper_path}/main -m {whisper_path}/models/{model_name} -l en -ovtt -mc 0 -bo 8 -f {audio_path} -o {transcription_path}", shell=True)
    
    # Duration of the video
    duration = get_video_duration(outpath + "/" + jobname + ".mp4")

    # Extract the text
    extracted_text = extract_every_third_line(transcription_path, 0, 3)[1:]
    
    # Extract the time
    extracted_times = extract_every_third_line(transcription_path, 1, 3)
    
    # Should be a one to one mapping between times and text
    # Thus, if we define a certain interval, then we should be able to get a
    # map of time to certain words
    
    # Create a time to key word mapping for a bin of time
    
    binned_time_dict = ""

    # Extract keywords from the transcription
    # Modify this function
    extracted_words = extract_words(binned_time_dict)

    with open(keywords_path, 'w') as f:
        json.dump(keywords, f)
    
    print(f"Transcription and keyword extraction completed. Files saved to {outpath}")

def get_vid_material(url, jobname):
    yt = YouTube(url)

    video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    video_stream.download(filename = jobname + ".mp4")

# Write a function for counting words
# Modify the function such that it takes in a dictionary
def extract_words(text):
    all_words = text.split(sep = " ")
    
    word_json_out = {}
    
    for word in all_words:
        cleaned_word = word.strip(" ")
        cleaned_word = cleaned_word.strip("\n")
        cleaned_word = cleaned_word.strip("\t")
        
        if cleaned_word not in word_json_out:
            word_json_out.update({cleaned_word:1})
            
        else:
            word_json_out[cleaned_word] += 1

    return word_json_out

# Write a function for analyzing the counts of extracted words
def analyze_extractedwords(word_json):
    print(word_json)

# Usage example
whisper_path = "/path/to/whisper"

# Auto generae a list of links to run it
youtube_link = "https://www.youtube.com/watch?v=example"

# Generate new names based on this
jobname = "example_video"
model_name = "base"
outpath = "/path/to/output"

generate_transcription_and_keywords(whisper_path, youtube_link, jobname, model_name, outpath)


