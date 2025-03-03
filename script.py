from PIL import Image, ImageDraw, ImageFont
import subprocess
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.realpath(__file__))

# Set the relative path for FFmpeg executable
ffmpeg_path = os.path.join(script_dir, 'ffmpeg.exe')  # Make sure FFmpeg is in the same directory as the script

# Check if FFmpeg is present
if not os.path.exists(ffmpeg_path):
    print("FFmpeg executable not found. Please ensure 'ffmpeg.exe' is in the same folder as this script.")
    exit(1)

def overlay_text(image_path, text, output_image_path, font_path="arial.ttf"):
    # Load the image using Pillow
    image = Image.open(image_path)
    # Create a drawing context to overlay text on the image
    draw = ImageDraw.Draw(image)
    
    try:
        # Try to load the specified font
        font = ImageFont.truetype(font_path, 400)
    except IOError:
        # If custom font is not found, fall back to the default font
        font = ImageFont.load_default()
    
    # Calculate the width and height of the text to center it on the image
    text_width, text_height = draw.textbbox((0, 0), text, font=font)[2:4]
    position = (image.width // 2 - text_width // 2, 10)  # Centered horizontally, positioned near the top

    
    # Overlay the text onto the image
    draw.text(position, text, fill="Black", font=font)
    
    # Save the image with the text overlay
    image.save(output_image_path)

def apply_transformation(image_path, transformation, output_image_path):
    # Open the image
    image = Image.open(image_path)
    
    # Apply the chosen transformation
    if transformation == 'grayscale':
        image = image.convert("L")  # Convert to grayscale
    elif transformation == 'rotate':
        image = image.rotate(45)  # Rotate image by 45 degrees
    elif transformation == 'resize':
        image = image.resize((640, 480))  # Resize the image to 640x480
    
    # Save the transformed image
    image.save(output_image_path)

def create_video(image_path, music_path, output_video_path, duration=5):
    # FFmpeg command to create a video from the image
    cmd = [
        ffmpeg_path,
        '-loop', '1',  # Loop the image
        '-i', image_path,  # Input image
        '-t', str(duration),  # Set the duration of the video in seconds
        '-c:v', 'libx264',  # Use H.264 codec for video
        '-r', '30',  # Set the frame rate to 30 frames per second
        '-pix_fmt', 'yuv420p',  # Set pixel format
        '-vf', 'scale=1280:720',  # Resize the video to 1280x720 resolution
        '-y',  # Overwrite the output video file if it already exists
        output_video_path  # Path to save the output video
    ]
    
    try:
        # Run the FFmpeg command to create the video
        result = subprocess.run(cmd, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"FFmpeg Output: {result.stdout.decode()}")
        print(f"FFmpeg Error Output: {result.stderr.decode() if result.stderr else 'No error output'}")
    
    except subprocess.CalledProcessError as e:
        # Handle any errors during video creation
        print(f"Error during video creation: {e.stderr.decode()}")

    # FFmpeg command to add background music to the video
    cmd = [
        ffmpeg_path,
        '-i', output_video_path,  # Input video file
        '-i', music_path,  # Input music (audio file)
        '-c:v', 'copy',  # Copy the video stream without re-encoding
        '-c:a', 'aac',  # Use AAC audio codec
        '-strict', 'experimental',  # Allow experimental codecs
        '-shortest',  # Stop the video when the shortest stream (audio/video) ends
        '-y',  # Overwrite the output file if it already exists
        'output_with_audio.mp4'  # Path to save the final video with audio
    ]
    
    try:
        # Run the FFmpeg command to add background music
        result = subprocess.run(cmd, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"FFmpeg Output: {result.stdout.decode()}")
        print(f"FFmpeg Error Output: {result.stderr.decode() if result.stderr else 'No error output'}")
    
    except subprocess.CalledProcessError as e:
        # Handle any errors during audio addition
        print(f"Error during audio addition: {e.stderr.decode()}")

def main(image_path, text, music_path, output_video_path, font_path="arial.ttf", transformation="grayscale"):
    # Temporary path to save the transformed image
    transformed_image_path = "transformed_image.jpg"
    
    # Step 1: Overlay the text on the image
    overlay_text(image_path, text, transformed_image_path, font_path)
    
    # Step 2: Apply the selected transformation (grayscale, rotate, or resize)
    apply_transformation(transformed_image_path, transformation, transformed_image_path)
    
    # Step 3: Create a video from the transformed image and add background music
    create_video(transformed_image_path, music_path, output_video_path, duration=5)

if __name__ == "__main__":
    # The directory where the script is located
    script_dir = os.path.dirname(os.path.realpath(__file__))
    
    #Paths to the image, music, and font files using relative paths
    image_path = os.path.join(script_dir, "input_image.jpg")  
    text = "Beautiful Scenery"  # Text to overlay on the image
    music_path = os.path.join(script_dir, "background_music.mp3")  
    output_video_path = os.path.join(script_dir, "output_video.mp4")  # Output video path
    
    # Specify font and transformation type
    font_path = os.path.join(script_dir, "ARIAL.ttf")  
    transformation = "grayscale"  # Can be "grayscale", "rotate", or "resize"
    
    # Run the main function
    main(image_path, text, music_path, output_video_path, font_path, transformation)
