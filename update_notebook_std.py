import json
import os

notebook_path = '/Users/j/Documents/OC_Inge_IA/Projet_6/Projet_6_feature_image_AG.ipynb'

new_cells = [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Image Standardization & Preprocessing\n",
    "Steps: Aspect Ratio analysis, Resize to 224x224 (with padding), Pixel Normalization."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from PIL import Image, ImageOps\n",
    "import numpy as np\n",
    "import os\n",
    "\n",
    "# 1. Analyze Aspect Ratios & Orientations\n",
    "widths, heights, ratios = [], [], []\n",
    "\n",
    "img_dir = 'data/Flipkart/Images/complete_dataset'\n",
    "sample_size = min(500, len(df)) # Check first 500 for speed\n",
    "\n",
    "for img_name in df.index[:sample_size]:\n",
    "    img_path = os.path.join(img_dir, img_name)\n",
    "    if not os.path.exists(img_path):\n",
    "        continue\n",
    "    with Image.open(img_path) as img:\n",
    "        w, h = img.size\n",
    "        widths.append(w)\n",
    "        heights.append(h)\n",
    "        ratios.append(w / h)\n",
    "\n",
    "plt.figure(figsize=(12, 4))\n",
    "plt.subplot(1, 3, 1)\n",
    "sns.histplot(widths, kde=True).set_title('Width Distribution')\n",
    "plt.subplot(1, 3, 2)\n",
    "sns.histplot(heights, kde=True).set_title('Height Distribution')\n",
    "plt.subplot(1, 3, 3)\n",
    "sns.histplot(ratios, kde=True).set_title('Aspect Ratio (W/H) Distribution')\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2. Define Preprocessing Function (Resize + Pad + Normalize)\n",
    "def preprocess_image(image_path, target_size=(224, 224)):\n",
    "    \"\"\"\n",
    "    Opens image, corrects orientation, resizes with padding to target_size,\n",
    "    and normalizes pixels to [0,1].\n",
    "    \"\"\"\n",
    "    if not os.path.exists(image_path):\n",
    "        return None\n",
    "    \n",
    "    try:\n",
    "        img = Image.open(image_path)\n",
    "        \n",
    "        # Handle EXIF Orientation\n",
    "        img = ImageOps.exif_transpose(img)\n",
    "        \n",
    "        # Convert to RGB if not already\n",
    "        if img.mode != 'RGB':\n",
    "            img = img.convert('RGB')\n",
    "            \n",
    "        # Resize maintaining aspect ratio\n",
    "        img.thumbnail(target_size, Image.Resampling.LANCZOS)\n",
    "        \n",
    "        # Create a white canvas of target size\n",
    "        # (Using white background is common for product images)\n",
    "        new_img = Image.new(\"RGB\", target_size, (255, 255, 255))\n",
    "        \n",
    "        # Paste resized image in center\n",
    "        left = (target_size[0] - img.size[0]) // 2\n",
    "        top = (target_size[1] - img.size[1]) // 2\n",
    "        new_img.paste(img, (left, top))\n",
    "        \n",
    "        # Convert to numpy array and normalize [0, 1]\n",
    "        img_array = np.array(new_img, dtype=np.float32) / 255.0\n",
    "        \n",
    "        return img_array\n",
    "        \n",
    "    except Exception as e:\n",
    "        print(f\"Error processing {image_path}: {e}\")\n",
    "        return None"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 3. Visualize Before vs After\n",
    "def show_comparison(img_names, img_dir):\n",
    "    plt.figure(figsize=(15, 5))\n",
    "    for i, img_name in enumerate(img_names):\n",
    "        img_path = os.path.join(img_dir, img_name)\n",
    "        \n",
    "        # Original\n",
    "        if not os.path.exists(img_path): continue\n",
    "        orig = Image.open(img_path)\n",
    "        \n",
    "        # Processed\n",
    "        processed = preprocess_image(img_path)\n",
    "        \n",
    "        # Plot Original\n",
    "        plt.subplot(2, len(img_names), i + 1)\n",
    "        plt.imshow(orig)\n",
    "        plt.title(f\"Orig: {orig.size}\")\n",
    "        plt.axis('off')\n",
    "        \n",
    "        # Plot Processed\n",
    "        plt.subplot(2, len(img_names), len(img_names) + i + 1)\n",
    "        plt.imshow(processed)\n",
    "        plt.title(f\"Norm: {processed.shape}\")\n",
    "        plt.axis('off')\n",
    "    plt.tight_layout()\n",
    "    plt.show()\n",
    "\n",
    "# Pick 5 random images to test\n",
    "sample_images = df.sample(5).index.tolist()\n",
    "show_comparison(sample_images, img_dir)"
   ]
  }
]

with open(notebook_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Append new cells
data['cells'].extend(new_cells)

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=1)

print("Notebook updated with standardization cells.")
