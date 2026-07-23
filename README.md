# Football Player and Ball Detection with YOLOv5

This project applies [Ultralytics YOLOv5](https://github.com/ultralytics/yolov5) to football footage. The custom dataset contains two object classes—`player` and `ball`—and the repository includes the scripts required to train, validate, and run inference on images or videos.

| Language   | Guide                                                                                                 |
| ---------- | ----------------------------------------------------------------------------------------------------- |
| English    | [Overview](#overview) · [Quick start](#quick-start) · [Training](#training) · [Inference](#inference) |
| Tiếng Việt | [Hướng dẫn nhanh bằng tiếng Việt](#hướng-dẫn-nhanh-bằng-tiếng-việt)                                   |

## Demo

The following file is a sample detection result generated in `runs/detect`:

<video src="runs/detect/exp3/Match_1953_2_0_subclip.mp4" controls width="100%">
  Your browser does not support embedded video. Use the link below to open the result.
</video>

**[Watch or download the detection output](runs/detect/exp3/Match_1953_2_0_subclip.mp4)**

> GitHub may show the video as a downloadable file instead of an inline player, depending on the browser. The direct link above remains available in either case.

## Overview

- **Task:** object detection in football videos
- **Classes:** `player`, `ball`
- **Framework:** PyTorch and YOLOv5
- **Dataset configuration:** [`football.yaml`](football.yaml)
- **Detection outputs:** `runs/detect/`
- **Supported input:** images, videos, folders, webcams, and network streams

## Project structure

```text
.
├── data/                   # YOLOv5 dataset definitions and utilities
├── models/                 # YOLOv5 model architectures
├── runs/detect/            # Generated inference results
├── utils/                  # Shared YOLOv5 utilities
├── detect.py               # Run object detection
├── train.py                # Train a model
├── val.py                  # Validate a model
├── football.yaml           # Football dataset and class configuration
└── requirements.txt        # Python dependencies
```

Large datasets, model checkpoints, caches, IDE settings, and generated experiment folders are excluded from Git. One curated output video under `runs/detect/exp3` is intentionally included for this README demo.

## Requirements

- Python 3.8 or newer
- Git
- PyTorch
- An NVIDIA GPU with CUDA is recommended for training, but CPU inference is supported

## Quick start

Clone the repository, create a virtual environment, and install the dependencies:

```bash
git clone <your-repository-url>
cd yolov5

python -m venv .venv
```

Activate the environment:

```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

```bash
# Linux or macOS
source .venv/bin/activate
```

Then install the project dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Check whether PyTorch can use CUDA:

```bash
python exam.py
```

## Dataset

The dataset must use the standard YOLO directory structure:

```text
football_dataset/
├── images/
│   ├── train/
│   └── val/
└── labels/
    ├── train/
    └── val/
```

Each label line uses the YOLO format:

```text
class_id x_center y_center width height
```

All coordinates are normalized to the range `0–1`. Update the `path` value in [`football.yaml`](football.yaml) so that it points to the dataset on your machine.

## Training

Train a YOLOv5s model from pretrained weights:

```bash
python train.py --img 640 --batch 16 --epochs 100 --data football.yaml --weights yolov5s.pt --name football-yolov5s
```

Training artifacts are written to `runs/train/football-yolov5s`. These generated artifacts are ignored by Git. Keep final checkpoints in external storage or publish them through a GitHub Release instead of committing large binary files.

## Validation

Validate the best checkpoint:

```bash
python val.py --weights runs/train/football-yolov5s/weights/best.pt --data football.yaml --img 640
```

## Inference

Run detection on a video:

```bash
python detect.py --weights runs/train/football-yolov5s/weights/best.pt --source path/to/input.mp4 --name football-demo
```

Run detection on an image:

```bash
python detect.py --weights runs/train/football-yolov5s/weights/best.pt --source path/to/image.jpg
```

Run detection from a webcam:

```bash
python detect.py --weights runs/train/football-yolov5s/weights/best.pt --source 0
```

The annotated files are saved under `runs/detect/<experiment-name>/`.

## Hướng dẫn nhanh bằng tiếng Việt

| Nội dung        | Hướng dẫn                                                                                                                   |
| --------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Mục tiêu        | Phát hiện `player` (cầu thủ) và `ball` (bóng) trong ảnh hoặc video bóng đá.                                                 |
| Cài đặt         | Tạo môi trường ảo, kích hoạt môi trường, sau đó chạy `pip install -r requirements.txt`.                                     |
| Dữ liệu         | Sửa trường `path` trong `football.yaml` để trỏ đến bộ dữ liệu trên máy của bạn.                                             |
| Huấn luyện      | Chạy `python train.py --img 640 --batch 16 --epochs 100 --data football.yaml --weights yolov5s.pt --name football-yolov5s`. |
| Nhận diện video | Chạy `python detect.py --weights <duong-dan-best.pt> --source <duong-dan-video>`.                                           |
| Kết quả         | Ảnh/video đã nhận diện được lưu trong `runs/detect/`.                                                                       |
| Video mẫu       | [Xem hoặc tải video kết quả](runs/detect/exp3/Match_1953_2_0_subclip.mp4).                                                  |

Nếu không có GPU NVIDIA, bạn vẫn có thể chạy bằng CPU nhưng tốc độ huấn luyện và nhận diện video sẽ chậm hơn.

## Git and repository hygiene

Before committing, review the files Git will include:

```bash
git status
git check-ignore -v path/to/file
```

Do not commit datasets, secrets, virtual environments, generated training runs, or model weights. The `.gitignore` file is configured to exclude these items while allowing the curated demo video used above.

## Acknowledgments

This repository is based on [Ultralytics YOLOv5](https://github.com/ultralytics/yolov5). Refer to the upstream [documentation](https://docs.ultralytics.com/yolov5/) for additional training, export, and deployment options.

## License

YOLOv5 is distributed under the [GNU Affero General Public License v3.0](LICENSE). Review the upstream Ultralytics licensing terms before commercial deployment.
