[English](README.md) | 简体中文

# HDR 图像转换与 ICC 配置文件嵌入

本项目演示了如何将图像转换为 Rec.2020 PQ 色彩空间并嵌入 ICC 配置文件以实现 HDR 显示。

## 项目结构

项目主要文件组织如下：

-   [`main.py`](main.py): 应用程序的主入口点。它协调色彩空间转换和 ICC 配置文件嵌入过程。
-   [`color_conversion.py`](color_conversion.py): 将图像色彩空间转换为 Rec.2020 PQ。
-   [`icc.py`](icc.py): 处理图像文件中 ICC 配置文件的提取和附加。

## 设置

要设置和运行此项目，请按照以下步骤操作：

1.  **克隆仓库：**
    ```bash
    git clone [repository_url]
    cd image-convert
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
