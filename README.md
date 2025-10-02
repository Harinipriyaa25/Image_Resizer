# 🖼️ Image Resizer Tool

This is a simple project I made to help resize and convert a bunch of images at once. Instead of opening every image and resizing it by hand, this script does it all for you automatically.

---

## 🎯 What it does

* Takes all the images from a folder (`images_input`)
* Resizes them to a maximum size (without stretching)
* Converts them to **JPEG** format
* Saves them neatly in another folder (`images_output`)
* Skips images if resizing would make them bigger than the original

---

## 🛠 What I used

* **Python** for writing the script
* **Pillow (PIL)** library for working with images

---

## 🚀 How to use it

1. Install Python and make sure Pillow is installed:

   bash
   pip install pillow
   ```

2. Put all the images you want to resize inside the folder called `images_input`.

3. Run the script:

   bash
  python Image_Resizer.py
   ```

4.Look inside the folder called `images_output` to find your resized images.

---

## ✅ Why this is useful

* No more manual resizing.
* Keeps the quality good while reducing file size.
* Perfect for preparing images for websites, projects, or sharing.

---

## 🌟 The outcome

You get an **automated image resizer** that saves time, keeps your pictures neat, and makes big image collections easier to handle.
