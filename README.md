# Video Creation Project

This project allows you to create a video from an image with an optional text overlay and background music. The Python script utilizes FFmpeg for video creation and audio integration.

## 🛠️ Requirements

### 1. **Python Packages**
You will need the following Python libraries:
- **Pillow**: For image processing.
- **subprocess**: For running FFmpeg commands.

To install the required packages, run:

pip install pillow

## 2. FFmpeg

FFmpeg is required for video creation and audio integration. It can be downloaded from [FFmpeg.org](https://ffmpeg.org/download.html).

### Installation Guide:

| Platform     | Steps                                                                 |
|--------------|-----------------------------------------------------------------------|
| **Windows**  | Download `ffmpeg.exe` and place it in the same directory as the script.|
| **Linux**    | Install using: `sudo apt install ffmpeg` (Ubuntu)                    |
| **macOS**    | Install using: `brew install ffmpeg`                                 |

Make sure that `ffmpeg.exe` (on Windows) or `ffmpeg` (on Linux/macOS) is available in your system's PATH or place it in the same folder as the script.

---

## 3. Font File

The script uses the `arial.ttf` font by default. You can provide your custom `.ttf` font if needed.

---

## 🗂️ Project Structure

/video_creation_project/
    |-- ffmpeg.exe              # FFmpeg executable (Windows)
    |-- input_image.jpg         # The image you want to use in the video
    |-- background_music.mp3    # Background audio to overlay in the video
    |-- ARIAL.ttf               # Font file for text overlay (optional)
    |-- script.py               # Main Python script containing the logic
    |-- transformed_image.jpg   # Temporary file for the transformed image
    |-- output_video.mp4        # Final video with text and audio

## ⚡ Usage

### 1. **Prepare Your Files**

Ensure the following files are in the same directory as the script:

- **Image file**: (e.g., `input_image.jpg`)
- **Background music file**: (e.g., `background_music.mp3`)
- **Font file (optional)**: (e.g., `ARIAL.ttf`)
- **Python script**: (`script.py`)

### 2. **Modify the Script (Optional)**

You can customize the following variables in the script:

| Variable         | Description                                                   |
|------------------|---------------------------------------------------------------|
| `text`           | Change the text that will be overlayed on the image.          |
| `transformation` | Choose the transformation to apply (`"grayscale"`, `"rotate"`, or `"resize"`). |
| `font_path`      | Provide a custom font (optional, default: `ARIAL.ttf`).       |

### 3. **Run the Script**

Once everything is set up, run the Python script:

python script.py


### 4. **Output**

The script generates a 5-second video by default, with the following features:

| Feature             | Description                                                         |
|---------------------|---------------------------------------------------------------------|
| **Text Overlay**     | The specified text will be displayed on the image.                  |
| **Transformation**   | Grayscale, rotate, or resize effect will be applied to the image.   |
| **Background Music** | Your provided audio will be added to the video.                     |

The final output video is saved as `output_video.mp4` in the same directory. If background music is added, the video will be saved as `output_with_audio.mp4`.

### 5. **Customization**

You can adjust these settings as per your needs:

| Setting             | Description                                                       |
|---------------------|-------------------------------------------------------------------|
| **Video Duration**   | Modify the `duration` parameter in the `create_video()` function. |
| **Video Resolution** | Adjust the resolution in the `scale` parameter (e.g., `scale=1280:720`). |
| **Text Styling**     | Customize the font size, color, and position in the `overlay_text()` function. |

---

## 🔧 Technical Details

### 1. **Text Overlay**

The text is centered horizontally at the top of the image. You can change the positioning, font size, and text color to suit your needs.

### 2. **Transformations**

Currently, the script supports three transformations:

| Transformation   | Description                                                       |
|------------------|-------------------------------------------------------------------|
| **Grayscale**    | Converts the image to black-and-white.                            |
| **Rotation**     | Rotates the image by 45 degrees.                                  |
| **Resize**       | Resizes the image to a fixed resolution (default: 640x480).       |

### 3. **Video Creation**

The script uses FFmpeg to create a video from the image. The video is generated at 30 frames per second, with a resolution of 1280x720, and encoded with the H.264 codec for maximum compatibility.

### 4. **Audio Integration**

FFmpeg is also used to add background music to the video. The video duration is matched with the length of the audio, ensuring the video ends when the audio stops.

---

## 🌟 Example Workflow

Imagine you're creating a short promo video for a travel blog:

| Step           | Description                                                          |
|----------------|----------------------------------------------------------------------|
| **Image**      | Use a stunning landscape photo (`input_image.jpg`).                  |
| **Text**       | Add the text "Explore the World" in a beautiful font, centered at the top. |
| **Transformation** | Apply the **grayscale** effect to give the video a vintage feel.  |
| **Music**      | Add a soothing background track (`background_music.mp3`) to set the mood. |
| **Video**      | Create a 5-second video that loops the image with the text and music. |

---

## 💡 Potential Use Cases

| Use Case           | Description                                                         |
|--------------------|---------------------------------------------------------------------|
| **Content Creation**| Quickly generate promotional or highlight videos for social media platforms. |
| **Marketing**       | Enhance product showcases with custom text and background music.   |
| **Personal Projects**| Transform your photos into engaging videos for family or friends. |

---


## 👨‍💻 Contact

If you have any questions, feel free to reach out:

- **Email**: maanparveen47@gmail.com
- **LinkedIn**: [Your LinkedIn Profile](https://www.linkedin.com/in/parveenmaan)

Happy Coding! 🎉
