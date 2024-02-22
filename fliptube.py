from pytube import YouTube
from moviepy.editor import VideoFileClip, VideoClip , vfx
from moviepy.editor import concatenate_videoclips

def download_youtube_video(url, output_path, yt_title):
    yt = YouTube(url)
    yt.title = yt_title
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path)

    print(output_path)

def flip_video_horizontal(input_path, output_path):
    clip = VideoFileClip(input_path)
    flipped_clip = clip.fx(vfx.mirror_x)
    flipped_clip.write_videofile(output_path, codec='libx264')
    clip.close()
    flipped_clip.close()

if __name__ == "__main__":
    youtube_url = input("Enter YouTube video URL: ")
    download_path = input("Enter download directory path: ")
    yt_title = input("Give the video a title: ")

    # Download YouTube video
    print("Downloading video...")
    download_youtube_video(youtube_url, download_path,yt_title)
    print("Video downloaded successfully!")

    # Flip the downloaded video horizontally
    video_file = download_path + "/"+ yt_title + ".mp4"
    output_file = download_path + "/" + yt_title +"-flipped_video.mp4"
    print("Flipping video horizontally...")
    flip_video_horizontal(video_file, output_file)
    print("Video flipped successfully!")
