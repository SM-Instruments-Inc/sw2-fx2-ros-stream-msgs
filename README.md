# BATCAM FX2 Stream Message for ROS 2

> **This repository is no longer updated and will be archived.**
>
> BATCAM FX2 firmware **v1.1.1 and later** uses `fx2_stream_msgs` 2.0.0 from
> <https://gitlab.com/smins-oss/sound-camera/framework/protocol/fx-stream-msgs>.
>
> This repository stays at 1.2.0, the version used by firmware v1.1.0 and earlier.
> The two versions are not wire compatible, so build the version that matches
> the firmware on your device.

Custom ROS 2 message definitions for the BATCAM FX system.

To build this package, make sure all Python dependencies are installed:

```bash
pip install -r requirements.txt
```

Built and tested with Python 3.12 / ROS 2 Jazzy (Ubuntu 24.04 or later) / Yocto Scarthgap
Target compatibility: ROS 2 Humble (Ubuntu 22.04 or equivalent)

# Message Types

See [MessageType.md](MessageType.md) for the full list of message definitions.

That file is generated from `msg/` — regenerate it after changing any definition:

```bash
python generate_msg_docs.py
```
