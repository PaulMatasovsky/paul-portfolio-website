# Computer Helper — Device and User Notes

**AI-led project** · Hardware details reported so far; not verified in person · Updated October 28, 2026

## What I know

| Item | Uncle's Windows PC | Mom's Mac |
| --- | --- | --- |
| Computer | Dell OptiPlex 5070, probably Small Form Factor; case still needs checking | Mac mini, reportedly bought new around 2025 |
| Operating system | Windows 11 | macOS; version unknown |
| Processor | Intel Core i5-8500, 3.0 GHz | Chip not checked |
| Memory | 16 GB; module count and slots unknown | Not checked |
| Graphics | Intel UHD 630 integrated graphics; 128 MB reported as reserved graphics memory | Not checked |
| SSD and available storage | Not checked | Not checked |
| Browser, speakers, microphone | Not checked | Not checked |
| Screen/accessibility permissions | Not tested | Not tested |

I'm not buying RAM or a graphics card yet. We talked about 32 GB as a possible comfortable target, but it isn't a requirement until we've measured the assistant on the existing 16 GB system. If we consider a graphics card, I'll first confirm the SFF case, slots, power supply, and clearance.

## How my uncle uses his computer

He mainly uses email and LibreOffice to type letters. LibreOffice is installed and pinned to the Windows taskbar. His most common needs are finding downloaded documents outside Downloads and getting oriented when Windows feels busy. He's been using computers for roughly the past dozen years, mostly for these familiar tasks. I want the helper to use his own wording and avoid unnecessary computer jargon.

These observations are a starting point, not a completed usability survey. I've recorded [sample tasks and conversations](Uncle_Use_Cases_and_Conversation_Tests.md) separately.

## What I'll check next

On Windows, Task Manager → Performance → Memory should show installed memory and may show how many slots are in use. I can also run this **read-only** PowerShell command to list the installed modules:

```powershell
Get-CimInstance Win32_PhysicalMemory |
  Select-Object DeviceLocator, @{Name='GB';Expression={$_.Capacity / 1GB}}, Speed, PartNumber
```

On the Mac, About This Mac should show the chip and memory. I'll also check both systems' storage, browser, microphone, speakers, and accessibility permissions.

## What I'll ask each person

1. What do you most often need help with?
2. Would you rather type, speak, or press a Help button?
3. Is it easier to get one instruction at a time?
4. Would you be comfortable letting the helper inspect the screen when you ask?
5. What should happen if the assistant doesn't know the answer?
6. How do you currently manage sign-ins and passwords?

I'll keep their answers private. Passwords, recovery information, service tags, device IDs, and personal screenshots don't belong in GitHub.
