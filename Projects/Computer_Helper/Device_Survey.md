# Device and User Survey

**Project classification:** **AI-led** · **Documentation updated:** 2026-10-28

**Status:** Not yet collected. This is a blank template; I'll keep completed personal notes private.

## Computer details

| What I need to know | Windows computer | Mac |
| --- | --- | --- |
| Operating system and version | To check | To check |
| Processor / chip | To check | To check (Intel or Apple silicon) |
| Memory (RAM) | To check | To check |
| Graphics / video memory | To check | To check |
| Free storage | To check | To check |
| Browser and main programs | To check | To check |
| Microphone, speakers and any display needs | To check | To check |
| Screen-sharing / accessibility permissions | To test | To test |

## Questions I'll ask

1. What do you most often need help doing on the computer?
2. Would you rather type, talk, or press a button to ask for help?
3. Is it easier if someone gives you one instruction at a time?
4. Would you be comfortable letting the helper look at your screen when you ask it to?
5. What should the helper do when it cannot help?
6. How do you currently sign in to websites or keep track of passwords?

I'll ask permission before collecting information. Passwords, account details, recovery keys, device identifiers, and private screenshots will not go into GitHub.

## What we currently know (reported, not verified on site)

| Item | Windows machine | Mac |
| --- | --- | --- |
| Model | Dell OptiPlex 5070; **SFF believed, not confirmed** | Mac mini, reportedly purchased new around 2025 |
| Processor | Intel Core i5-8500, 3.0 GHz | Chip not yet checked |
| RAM | 16 GB installed; slot use unknown | Not checked |
| Graphics | Integrated Intel UHD 630; Windows reports 128 MB reserved graphics memory | Not checked |
| OS | Windows 11 | macOS version not checked |
| SSD, browser, microphone | Not checked | Not checked |
| Upgrade plans | RAM/GPU purchases postponed until prototype performance is measured | None decided |

**Budget decision:** Keep the existing Windows hardware for the first tests. We have discussed 32 GB as a possible comfortable target for a complete system, **not a current requirement**. The SFF chassis and power supply must be verified before considering a low-profile GPU. Do not buy parts from this survey alone.

When the Windows PC is accessible, check Task Manager's Memory page and run the read-only PowerShell query below. Do not post the computer's Service Tag, Device ID, or other unique identifiers publicly.

```powershell
Get-CimInstance Win32_PhysicalMemory |
  Select-Object DeviceLocator, @{Name='GB';Expression={$_.Capacity / 1GB}}, Speed, PartNumber
```

