import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    install_requires = fh.read().split('\n')

setuptools.setup(
    name="rich-LogConsole",
    version="1.0.1",
    author="Wankko Ree",
    author_email="wkr@wkr.moe",
    description="一个实现了在一定高度自动滚动的 rich 日志组件，有两种刷新方式，建议配合Layout、Panel等组件使用。",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GPLv3",
    url="https://github.com/WankkoRee/rich-LogConsole",
    project_urls={
        "Bug Tracker": "https://github.com/WankkoRee/rich-LogConsole/issues",
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: English",
    ],
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    python_requires=">=3.7",
)
