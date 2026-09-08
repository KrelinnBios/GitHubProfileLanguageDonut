# AGENTS.md

本文件适用于整个仓库，作为 AI 编码代理修改本项目时的项目规范。除非用户另有要求，使用中文回复和说明。

## 项目概览

GitHub Profile Language Donut Chart 是一个基于 Python 标准库实现的 composite GitHub Action，用于读取公开仓库语言数据、生成适合 GitHub Profile README 的主题自适应 SVG 环形图，并维护 README 中的版本化图片引用。

- `action.yml`：Action 输入、输出和执行入口。
- `src/generate.py`：命令行入口与整体生成流程。
- `src/language_donut/github.py`：GitHub 仓库与 Languages API 数据读取。
- `src/language_donut/config.py`：配置加载与默认值。
- `src/language_donut/chart.py`：SVG 布局与渲染。
- `src/language_donut/colors.py`：语言颜色规则。
- `src/language_donut/output.py`：版本化文件名、README 引用更新与旧图清理。
- `tests/`：布局、汇总、配色和输出行为测试。
- `examples/`：配置、工作流和预览示例。

项目不依赖第三方 Python 包，保持可直接运行于 GitHub 托管 runner 的轻量实现。

## 开始任务前

- 先读取与任务直接相关的模块、测试和示例，不根据 README 描述或文件名猜测实际实现。
- 修改 Action 输入、输出或默认值时，同时检查 `action.yml`、配置模块、示例工作流和三种语言 README。
- 修改 SVG 布局、颜色或语言汇总逻辑时，先检查现有测试以及 `examples/` 中的预览生成方式。
- 优先做最小、可验证的改动，不为了局部需求引入第三方依赖、框架或无关重构。
- 工作区已有其他修改时保留无关内容，不批量格式化或清理。

## 修改原则

- 保持 Python 标准库实现，除非用户明确要求改变依赖策略。
- GitHub Languages API 返回的是语言字节数；百分比和排序继续以实际汇总数据为准，不把图表解释为熟练度、开发时长或提交次数。
- 默认排除个人主页仓库、Fork 和归档仓库；修改统计范围时同时检查配置兼容性和公开说明。
- 最多单独展示前 9 种语言，其余汇总为 `Other`；不要让汇总逻辑与图例、中心标签或百分比计算使用不同口径。
- 极小语言扇段的最低可见角度只影响 SVG 几何，不修改真实文字百分比。
- 未显式配置的语言颜色必须保持稳定，不能因运行顺序或一次执行随机变化。
- SVG 必须继续通过 `prefers-color-scheme` 适配 GitHub 浅色与深色模式。
- 不把敏感 Token、API 响应、用户本地配置或临时调试数据提交到仓库。

## 输出与缓存约束

- 生成文件使用内容摘要形成版本化文件名，以绕过 GitHub 对同名图片的缓存。
- `output.py` 负责更新 README 图片引用并清理旧版本文件；修改输出逻辑时必须保证三者一致：新 SVG 路径、README 引用、旧图清理。
- 数据和配置没有变化时，应保持幂等，避免无意义地生成新文件或让 `changed` 变为 `true`。
- 首次运行仍需兼容 README 中未版本化的占位路径，例如 `./language-donut.svg`。
- `action.yml` 的 `image` 与 `changed` 输出语义不得与实际生成逻辑漂移。

## 验证

代码修改至少运行：

```bash
python -m unittest discover -s tests -v
```

修改 SVG 布局、主题、图例或配色时，额外生成并检查示例预览，确认：

- 1–5 种语言保持单列布局。
- 6–9 种语言正确切换为两列布局。
- 10 种及以上正确汇总为前 9 项加 `Other`。
- 浅色与深色主题文字、轨道和扇段均可辨认。
- 未知语言颜色稳定。
- README 引用、版本化文件名和旧图清理符合预期。

纯文档修改无需运行测试，但应检查三种语言 README 的事实是否仍一致。

## 文档同步

- `README.md`、`README.zh-TW.md` 和 `README.en.md` 面向使用者；`AGENTS.md` 只记录编码代理修改项目时需要遵守的规则。
- 三种语言 README 的结构、Action 输入输出、配置字段、统计口径和使用步骤保持一致。
- 修改 `action.yml`、配置字段、默认布局、统计范围、版本化文件行为或隐私边界时，检查三种语言 README 和 `examples/` 是否需要同步。
- 示例中的 Action 版本解析和工作流行为应与当前正式使用方式保持一致。

## 提交约定

- 一个提交聚焦一个明确主题。
- 提交信息简短说明实际结果。
- 不提交测试临时文件、API 响应、令牌、本地配置或与任务无关的生成物。
- 工作区已有其他修改时，只处理并提交本次任务涉及的内容。