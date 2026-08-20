# 第三方软件、内容与服务说明

本文件补充 [LICENSE](./LICENSE)，用于说明 GitHub Profile Language Donut Chart 所使用、但不由本项目 MIT License 重新授权的第三方软件、数据和外部服务。具体文件或内容旁如有更明确的权利声明，以该声明为准。

## 第三方软件与资源

本项目运行时仅使用 Python 标准库，不随项目分发需要单独声明许可证的第三方 Python 软件包。示例工作流使用 GitHub Actions 官方维护的 `actions/checkout`，其许可证和权利声明以对应版本仓库为准。

上述软件不会因为被本项目引用、运行或分发而改用本项目的 MIT License。

## GitHub 数据与生成内容

Action 通过 GitHub REST API 读取公开仓库和语言数据，并根据 GitHub Linguist 返回的数据生成 SVG。语言数据、仓库名称、GitHub、GitHub Actions 以及相关标识不属于本项目自身代码，也不因生成图表而纳入 MIT License。

生成的 SVG 和被更新的 README 内容由使用者提交到自己的仓库；使用者应自行确认其中数据、名称、图片和其他内容的权利与隐私边界。

## 外部服务

运行时可能访问 GitHub REST API、GitHub Releases 和 GitHub Actions。这些服务的可用性、访问控制、日志处理、隐私政策和服务条款由各自运营方负责，本项目不控制这些服务。

## 版本与反馈

Action 的输入、输出和运行方式以 [action.yml](./action.yml) 及本仓库文档为准。完整许可证文本及上游版权声明以各项目发布内容为准；本文中的许可证标识和链接仅用于定位，不替代相应许可证正文。

本项目使用或展示第三方材料，不代表 GitHub Profile Language Donut Chart 有权对其重新许可，也不代表相关权利人对本项目作出认可或背书。如发现版本、来源或权利标注不完整，请通过 [GitHub Issue](https://github.com/KrelinnBios/github-profile-language-donut/issues) 反馈。
