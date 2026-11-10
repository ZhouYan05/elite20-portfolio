# ZhouYan_C10H_安装记录：Hermes Agent 安装全过程（真实尝试）

> 任务：C10H 安装并驾驭 Hermes Agent（Level 1：安装与首次对话）
> 目标平台：Windows 11 Home 10.0.26100（学校设备，**无管理员权限**）
> 日期：2026-11-10 ｜ 结论：**安装受限于环境权限，4 条官方路径全部实测受阻；配置方案已就绪，待有管理员权限的环境即可执行。**

---

## 一、前置事实（来自 C10H 规范）

- Hermes Agent（github.com/NousResearch/hermes-agent）官方支持：**Linux / macOS / WSL2**，**不支持原生 Windows**；
- 环境要求：Python 3.11+、Node.js（安装脚本会处理）、需能访问 GitHub；
- 因此 Windows 上的唯一官方路径是 **WSL2**。

## 二、实测尝试链（4 条路径，全部真实执行）

### 尝试 1：检查 WSL 现状

```powershell
> wsl --status
未安装用于 Linux 的 Windows 子系统。
可通过运行 wsl.exe --install 进行安装。
```

**结果**：WSL 特性未启用（符合预期，这是新机器常见状态）。

### 尝试 2：官方安装命令

```powershell
> wsl --install
（重复上述提示，安装未实际执行）
```

**结果**：命令返回帮助提示而不启动安装——因为 WSL 是 Windows 可选特性，需先启用特性（此步需要管理员权限）。

### 尝试 3：查询可选特性状态

```powershell
> Get-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
COMException：你的操作需要提升权限
```

**结果**：**权限拒绝**——连「查询特性状态」都需要管理员。

### 尝试 4：DISM 直接启用特性

```powershell
> dism /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
错误：需要提升权限才能运行 DISM。使用提升的命令提示符完成这些任务。
```

**结果**：**权限拒绝**。尝试用 `Start-Process -Verb RunAs` 提权时，系统弹出 UAC 窗口——本机账号不在管理员组，无法批准。

## 三、结论与判定

| 判定项 | 结论 |
|---|---|
| 是否是我操作流程的问题 | 否——按微软官方文档的标准路径全部执行，每一步的输出已存档（`_install_attempt.txt`） |
| 卡点 | Windows 可选特性启用必须管理员权限；本机为受限账号 |
| 官方替代路径 | 无（Hermes 不支持原生 Windows；Docker Desktop 安装同样需要管理员） |
| 完成度 | Level 1 的「安装与首次对话」无法在本机完成；**配置方案与迁移清单已全部就绪**（见配置说明） |

## 四、证据

- 命令级证据：`_install_attempt.txt`（4 条命令的原始输出）
- 可视化证据：`ZhouYan_C10H_demo.png`（关键输出与结论摘要）

## 五、已完成的准备（可立即迁移的部分）

1. **环境核对清单**：Python 3.13.5 ✅（本机已有）、Node.js ✅（CogSeed 自带运行时可用）、网络可访问 GitHub ✅（gh CLI 正常）；
2. **安装脚本研读**：已阅读 Hermes 安装脚本与文档，理解其流程（clone → 依赖安装 → 初始化配置 → CLI 启动），迁移后可按步骤直接执行；
3. **首轮对话预案**：按 Level 1 要求「让 Hermes 帮我做一件事」——计划首个任务为「用 Hermes 读取本机 C10 技能库并生成技能使用周报」；
4. **配置说明文档**：`ZhouYan_C10H_配置说明.md`（拿来主义的「怎么配置的、在哪里个性化」已预先规划）。

## 六、后续计划

- 短期：向机房/学校申请管理员权限的一次性使用（如获批，按配置说明在 30 分钟内完成安装）；
- 替代：借用同学的 Linux 环境或云主机执行安装（配置说明可直接照搬）；
- 在安装完成前，C10 智能体按原计划独立运行（C10H 规范：完成 C10H 可加分，C10 本身已独立完成）。
