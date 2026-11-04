<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://readme-typing-svg.demolab.com?font=Inter&weight=800&size=36&duration=4000&pause=1000&color=F8FAFC&center=true&vCenter=true&width=700&height=70&lines=Hi%2C+I'm+Ritviz+Aggarwal;Electronics+Engineer;Embedded+and+Digital+Hardware">
  <source media="(prefers-color-scheme: light)" srcset="https://readme-typing-svg.demolab.com?font=Inter&weight=800&size=36&duration=4000&pause=1000&color=0F172A&center=true&vCenter=true&width=700&height=70&lines=Hi%2C+I'm+Ritviz+Aggarwal;Electronics+Engineer;Embedded+and+Digital+Hardware">
  <img alt="Hi, I'm Ritviz Aggarwal" src="https://readme-typing-svg.demolab.com?font=Inter&weight=800&size=36&duration=4000&pause=1000&color=F8FAFC&center=true&vCenter=true&width=700&height=70&lines=Hi%2C+I'm+Ritviz+Aggarwal;Electronics+Engineer;Embedded+and+Digital+Hardware">
</picture>

</div>

I am an Electronics and Instrumentation Engineering student focused on digital hardware and embedded systems. I design printed circuit boards in Altium, write bare metal C firmware, and build digital logic in Verilog.

I like working close to the hardware: bringing up power rails, debugging buses with an oscilloscope and a logic analyzer, and finding timing problems in simulation. Recently I designed a custom STM32 development board, built a RISC-V processor in Verilog, and turned an NXP FRDM-MCXN236 board into a tilt controlled USB mouse with a Python tuning dashboard.

Alongside projects, I am building lab material for junior engineering students on the ASLKv2010 analog system lab kit.

## My Toolkit

### Hardware & EDA Tools

![Verilog](https://img.shields.io/badge/Verilog-000000?style=for-the-badge&logoColor=white)
![SystemVerilog](https://img.shields.io/badge/SystemVerilog-000000?style=for-the-badge&logoColor=white)
![RISC-V](https://img.shields.io/badge/RISC--V-231F20?style=for-the-badge&logo=riscv&logoColor=white)
![FPGA](https://img.shields.io/badge/FPGA-0052CC?style=for-the-badge&logo=intel&logoColor=white)
![Altium Designer](https://img.shields.io/badge/Altium_Designer-A5C85A?style=for-the-badge&logo=altium&logoColor=white)
![STM32](https://img.shields.io/badge/STM32-03234B?style=for-the-badge&logo=stmicroelectronics&logoColor=white)
![ARM Cortex-M4](https://img.shields.io/badge/ARM_Cortex--M4-0091BD?style=for-the-badge&logo=arm&logoColor=white)
![ARM Cortex-M33](https://img.shields.io/badge/ARM_Cortex--M33-0091BD?style=for-the-badge&logo=arm&logoColor=white)
![NXP MCUXpresso](https://img.shields.io/badge/NXP_MCUXpresso-0E5AA7?style=for-the-badge)
![USB HID](https://img.shields.io/badge/USB_HID-4A4A4A?style=for-the-badge)
![Icarus Verilog](https://img.shields.io/badge/Icarus_Verilog-4A4A4A?style=for-the-badge)
![Yosys](https://img.shields.io/badge/Yosys-4A4A4A?style=for-the-badge)
![NextPNR](https://img.shields.io/badge/NextPNR-4A4A4A?style=for-the-badge)
![Tina TI](https://img.shields.io/badge/Tina_TI-FF0000?style=for-the-badge&logo=texasinstruments&logoColor=white)

### Languages

![C](https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

### Research & Tooling

![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
## Hardware projects

| Project | What it is | Tools |
|---|---|---|
| [STM32F411 development board](https://github.com/Rizz-Vizz/stm32f411-dev-board) | Custom 4 layer board with an MPU-6050 IMU. I did the schematic, layout and manufacturing files, then brought up the power rails and wrote bare metal C for I2C communication with the IMU. | Altium Designer, STM32F411, ARM Cortex-M4, C |
| [RISC-V RV32I core](https://github.com/Rizz-Vizz/riscv-rv32i-core) | Single cycle processor with all 47 base instructions, memory mapped UART and GPIO, and a toolchain that runs compiled C programs. Timing problems were found in GTKWave. | Verilog, Icarus Verilog, GTKWave, C |
| [Tilt air mouse](https://github.com/Rizz-Vizz/tilt-air-mouse-mcxn236) | USB HID mouse on an NXP FRDM-MCXN236. Reads an I2C accelerometer, filters it, and turns tilt into cursor movement. A Python dashboard tunes it live. Measured 0 px idle drift and 30 of 30 clicks recognised. | C, ARM Cortex-M33, I2C, USB HID, UART, Python |
| [Hardware neural MAC unit](https://github.com/Rizz-Vizz/Hardware-Neural-MAC) | Multiply accumulate unit and ReLU built from Verilog logic, synthesised and routed for an FPGA and checked with testbenches. | Verilog, Yosys, NextPNR, Icarus Verilog |
| [LED chaser PCB](https://github.com/Rizz-Vizz/LED-Chaser-PCB-Design) | Full Altium flow for a 555 timer and CD4017 circuit: schematic, layout, design rule checks and Gerber files. | Altium Designer |
| [Semiconductor image restoration](https://github.com/Rizz-Vizz/KLArity-Semicon-Restoration-) | Deep learning pipeline that restores degraded semiconductor images, reaching 29.1 dB PSNR. Top placement at the SEMICON India KLA Hackathon. | PyTorch, Python, OpenCV |
| [DSP platform](https://github.com/Rizz-Vizz/dsp-platform) | Real time audio analysis and modification using Fourier analysis, STFT and phase vocoding. [Live demo](https://kymatics.streamlit.app/) | Python |

My web, app and AI projects are on my [portfolio](https://ritviz.netlify.app/).

<!-- 3D chart is off. To turn it on, delete this first line and the matching last line of this block.
<div align="center">

## GitHub Activity

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./profile-3d-contrib/profile-night-rainbow.svg">
  <source media="(prefers-color-scheme: light)" srcset="./profile-3d-contrib/profile-green.svg">
  <img alt="3D Contribution City" src="./profile-3d-contrib/profile-night-rainbow.svg">
</picture>

</div>
-->

<div align="center">

## Contact Me

<a href="mailto:ritviz.aggarwal@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
<a href="https://www.linkedin.com/in/ritviz-aggarwal-488bbb246/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
<a href="https://www.youtube.com/@ritvizaggarwal"><img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="YouTube"></a>
<a href="https://www.kaggle.com/ritvizaggarwal"><img src="https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white" alt="Kaggle"></a>
<a href="https://ritviz.netlify.app/"><img src="https://img.shields.io/badge/Portfolio-2563EB?style=for-the-badge&logo=react&logoColor=white" alt="Portfolio"></a>

</div>
