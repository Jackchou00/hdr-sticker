[English](README.md) | 简体中文

# HDR 图像转换与 ICC 配置文件嵌入

本项目演示了如何将图像转换为 Rec.2020 PQ 色彩空间并嵌入 ICC 配置文件以实现 HDR 显示。

## 项目结构

项目主要文件组织如下：

-   [`main.py`](main.py): 应用程序的主入口点。它协调色彩空间转换和 ICC 配置文件嵌入过程。
-   [`color_conversion.py`](color_conversion.py): 将图像色彩空间转换为 Rec.2020 PQ。
-   [`icc.py`](icc.py): 处理图像文件中 ICC 配置文件的提取和附加。
-   

## 示例图片

- ori_hdr_image/hdr_frog.png
- ori_hdr_image/hdr_mashiro.png

从 QQ 群聊中收集的两个 HDR 表情，嵌入的 ICC 有所不同，用于提取 ICC 文件，通过 main 中的`icc_source_image_path`选择。

- example.png

一个普通的表情，假设其色彩空间为 sRGB，它将被转换到 Rec.2020 PQ 空间中，并嵌入 ICC 文件。

## 设置

要设置和运行此项目，请按照以下步骤操作：

1.  **克隆仓库：**
    ```bash  
    git clone https://github.com/Jackchou00/hdr-sticker
    cd hdr-sticker 
    ```  

2.  **虚拟环境：**
    ```bash
    uv sync
    ```

## 使用方法

要处理图像，请运行 `main.py` 脚本：

```bash
uv run main.py
```

处理行为可通过 `config.toml` 配置：

```toml
[paths]
input_image          = "example.png"                 # 输入文件名
converted_image      = "output_image.png"            # 中间转换图片
icc_source_image     = "ori_hdr_image/hdr_frog.png"  # 提取 ICC 的图片
final_output_image   = "output_image_with_icc.png"   # 最终输出

[color_conversion]
peak_luminance = 1600   # HDR 峰值亮度（nits）
```

调整上述参数可选择原图 ICC 源、输出路径和 HDR 峰值亮度。

默认的输入图片是 `example.png`，输出是`output_image_with_icc.png`，QQ 中，“图片”是不能依靠 ICC 激发 HDR 亮度的，需要是“动画表情”的状态，一种方法是先发送图片，再长按选择“添加表情”。目前只有 iOS（OLED 设备）能够激发 HDR 亮度，macOS 和 Windows 的策略是 ICC Tone Mapping，使用本方法获得的表情基本也能够正常显示，安卓不能够正常显示。
