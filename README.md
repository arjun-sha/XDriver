<div align="center" style="text-align: center --force;">
  <h1 align="center" style="text-align: center --force; "><a href='https://playwright.dev'>X</a>Driver 🎭</h1>
  <a href="https://pypi.org/">
    <img src="https://img.shields.io/badge/pypi%20package-v0.0.1-orange" alt="PyPI version">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/python-%3E%3D3.10-orange" alt="Python Version">
  </a>
  <a href="https://playwright.dev/python/">
    <img src="https://img.shields.io/badge/playwright-v1.52.0-green" alt="Playwright Version">
  </a>
  <a href="https://github.com/PyCQA/isort">
        <img src="https://img.shields.io/badge/imports-isort-yellow.svg">
    </a>
    <a href="https://github.com/ambv/black">
        <img src="https://img.shields.io/badge/code%20style-black-black.svg">
    </a>
</div>

<div align="center" style="text-align: center --force;">
<h4 align="center">Scrape the Web Without Getting Blocked – Playwright Anti-Block Patch Tool</h4>
<p><b>XDriver</b> patches Playwright with a single command to bypass anti-bot systems and make your scraping sessions block-free. It modifies driver, CDP connections and python wrapper, helping you avoid detection. ❤️</p>
</div>


## Getting Started

### Installation

You can install **XDriver** using `pip`:

```shell
$ pip install x_driver
```

### Activate XDriver

To patch your Playwright installation for stealth scraping, run:

```shell
$ x_driver activate
```

This command modifies Playwright’s source code to bypass common bot detection systems, making your scraping scripts more undetectable.

### Running playwright

<div align="center" style="text-align: center --force;">
<img src="assets/banner.png" style="width: 80%; height: auto;" alt="Logo" />
</div>

Once XDriver is activated, you can **run your Playwright scripts just like you normally would**—no additional changes needed.

Here's a basic example:

```python
import asyncio
import re
from playwright.async_api import Playwright, async_playwright, expect

async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("http://example.com/")

    await context.close()
    await browser.close()

async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())
```

XDriver ensures your Playwright instance is patched for stealth, allowing you to scrape without getting blocked

### Deactivate XDriver

To restore Playwright to its original state, run:

```shell
$ x_driver deactivate
```

This safely reverts all changes made by XDriver, returning Playwright to its default configuration.

---

## Performance  

| Test                                      | Status                | Test                                      | Status                |
|-------------------------------------------|-----------------------|-------------------------------------------|-----------------------|
| [**CreepJS**](https://abrahamjuliot.github.io/creepjs/)  | ✅ 100% Anonymous | [**Cloudflare WAF**](https://www.cloudflare.com/zero-trust/interactive-demo/) | ✅ Passed |
| [**Rebrowser Bot Detector**](https://bot-detector.rebrowser.net/) | ✅ Passed all tests | [**Cloudflare Turnstile**](https://nopecha.com/demo/turnstile) | ✅ Passed |
| [**BrowserScan**](https://browserscan.net/) | ✅ 87% | [**Cloudflare Interstitial**](https://nopecha.com/demo) | ✅ Passed |
| [**nopecha.com Turnstile**](https://nopecha.com/captcha/turnstile) | ✅ Passed | [**Kasada**](https://www.kasada.io/) | ✅ Passed |
| **Datadome Interstitial** | ✅ Passed | **Perimeter X**  | ✅ Passed |
| **Imperva** ([ticketmaster.com](https://www.ticketmaster.com/)) | ✅ Passed | [**Fingerprints.com**](https://fingerprint.com/products/bot-detection/) | ✅ Passed |
| [**IP-API Bot Detection**](https://ip-api.com/) | ✅ Passed | [**Whoer.net**](https://whoer.net/) | ✅ High Anonymity |
| [**IPQualityScore Bot Detection**](https://www.ipqualityscore.com/) | ✅ Passed | [**TLS Fingerprint Detection**](https://tls.browserleaks.com/) | ✅ No Anomalies |
| [**JA3er Bot Detector**](https://ja3er.com/) | ✅ No Tracking | [**AmIUnique**](https://amiunique.org/fp) | ✅ No Unique |
| [**Cover Your Tracks (EFF)**](https://coveryourtracks.eff.org/) | ✅ Strong Protection |  |  |

<div align="center">
    <h4>Let's Connect</h4>
  <a href="https://www.linkedin.com/in/arjunshankar1/" target="_blank">
    <img src="https://skillicons.dev/icons?i=linkedin" width=37 />
  </a>
  <a href="mailto:arjun.sha2425@gmail.com" target="_blank">
    <img src="https://skillicons.dev/icons?i=gmail" width=37 />
  </a>
  <a href="https://www.linkedin.com/in/arjunshankar1/">
    <img src="https://skillicons.dev/icons?i=twitter" width=37 /><br>
  </a>
</div>