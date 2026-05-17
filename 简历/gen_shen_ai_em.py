#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成深圳消费电子AI电磁研究岗位简历（三份）
JD核心要点：PINN / Surrogate Model / Maxwell方程 / VAE / Metasurface / HFSS&CST
方向：混合型偏B（AI+电磁仿真），项目顺序：NSFC → NUDT(B) → 华为(B)
"""

import base64, os, re

PHOTO_PATH = 'd:/YXC/YXC_know/Resume/简历/avatar.png'
OUT_DIR    = 'd:/YXC/YXC_know/Resume/简历'

# ── 读取照片 ──────────────────────────────────────────────────────────────────
with open(PHOTO_PATH, 'rb') as f:
    PHOTO_B64 = base64.b64encode(f.read()).decode()

# ── 读取现有打印版 CSS（从华为诺亚B方向打印版抽取head） ────────────────────────
with open('d:/YXC/YXC_know/Resume/简历/尤栖冲_华为诺亚_B方向.html', encoding='utf-8') as f:
    PRINT_TEMPLATE = f.read()

# 提取 <head>...</head>（含CSS）
head_match = re.search(r'<head>.*?</head>', PRINT_TEMPLATE, re.DOTALL)
PRINT_HEAD = head_match.group(0)
PRINT_HEAD = PRINT_HEAD.replace(
    '尤栖冲 · 简历 · 华为诺亚方舟 B方向',
    '尤栖冲 · 简历 · AI电磁研究工程师（深圳）'
)

# ══════════════════════════════════════════════════════════════════════════════
# 内容区块（三份文件共享，差异由模板决定）
# ══════════════════════════════════════════════════════════════════════════════

INTENT = 'AI电磁仿真研究员 &nbsp;·&nbsp; 物理信息替代模型（PINN / Surrogate Modeling）工程师'

EDU = '''
<tr>
  <td class="edu-year">2022.09—2027.07（预计）</td>
  <td class="edu-school"><b>上海科技大学</b>（双一流）&nbsp; 电子科学与技术 &nbsp; 硕博连读</td>
  <td class="edu-rank">成绩前 1%</td>
</tr>
<tr>
  <td class="edu-year">2018.09—2022.06</td>
  <td class="edu-school"><b>安徽大学</b>（211双一流）&nbsp; 电子信息工程 &nbsp; 工学学士</td>
  <td class="edu-rank">3/123（保研推免）</td>
</tr>
'''
EDU_NOTE = '博士主修：深度学习、高阶分布式系统、天线理论与技术、矩阵计算 &nbsp;&nbsp; 导师：林丰涵 教授'

# ── 项目一：NSFC（主打，Surrogate Model + VAE + Maxwell） ─────────────────────
PROJ1 = '''
<div class="proj-block">
  <div class="proj-header">
    <span class="proj-period">2024.09—至今</span>
    <span class="proj-title">国家自然科学基金面上项目——AI for Science 电磁仿真替代模型（Surrogate Model）平台</span>
    <span class="proj-role">主要负责人（博士生主导）</span>
  </div>

  <p class="proj-para"><span class="proj-label">1. 研究目标：</span>针对麦克斯韦方程组/亥姆霍兹（Helmholtz）方程全波仿真耗时数小时至数天、百万级训练集在工程上不可行的根本瓶颈，<b>首次提出</b>从并行仿真基础设施到生成式逆向设计的完整替代模型（Surrogate Modeling）链路，将天线/超构表面电磁仿真加速 <b>5000×</b>、所需数据规模压缩至 <b>0.012%</b>，实现波动方程求解从"数天"到"秒级"的全链路突破。</p>

  <p class="proj-para"><span class="proj-label">2. 研究内容：</span>① 搭建<b>行业首个</b>数百台服务器并行仿真系统（直接调用 HFSS/CST API 进行分布式电磁任务调度），效率相比单机全波仿真提升 <b>300×</b>（单机单核仿真需 2–8 小时/样本，并行系统缩至分钟级），将百万级麦克斯韦方程组求解数据集从不可行变为可行。② <b>首次提出</b>无需物理先验知识的统计分布随机筛选法：所需数据规模降至原有的 <b>0.012%</b>，仿真成本降低 99%；开源后 GitHub 浏览量突破 <b>10 万</b>，天线/超构表面领域排名第一。③ 构建天线专用<b>变分自编码器（VAE）</b>替代模型：实现电磁结构↔散射参数双向映射，逆向设计时间缩至 <b>1 秒</b>（比 HFSS/CST 快 <b>5000×</b>），大型超构表面设计从数周缩至 <b>5 分钟</b>。④ 以特征模式分析（CMA）为物理信息约束（Physics-Informed），指导 ML 优化搜索在物理可行域内进行，突破低剖面天线增益带宽极限，提升 <b>20%</b>，超越现有文献最优。</p>

  <p class="proj-para"><span class="proj-label">3. 关键结果：</span><br>
  <b>替代模型基础设施：</b>行业首个百台级并行电磁仿真系统，<b>300×</b> 加速，直接兼容 HFSS/CST API。<br>
  <b>数据效率：</b>所需数据压缩至 <b>0.012%</b>，仿真成本降低 99%；GitHub 开源 <b>10 万+</b> 浏览，验证可复现。<br>
  <b>VAE 替代模型：</b>逆向设计 <b>1 秒</b>（比全波仿真快 <b>5000×</b>），超构表面设计从数周缩至 <b>5 分钟</b>。<br>
  <b>Physics-Informed 突破：</b>CMA 约束下增益带宽提升 <b>20%</b>，超越文献最优；ARIA 智能体 Bilibili 演示破万播放。</p>

  <p class="proj-para"><span class="proj-label">4. 研究成果：</span>发表 <i>Electromagnetic Science</i>（IEEE 期刊，Gold Open Access，已发表，第一作者）；<i>IEEE iWAT 2026</i>（已发表，唯一学生作者）；<i>ICMMT 2023</i>（已发表，唯一学生作者，GitHub 领域首篇开源）；<i>IEEE APCAP 2024</i>（已发表，唯一学生作者）。</p>
</div>
'''

# ── 项目二：NUDT（B版，DCVAE + Metasurface 55000条数据库） ───────────────────
PROJ2 = '''
<div class="proj-block">
  <div class="proj-header">
    <span class="proj-period">2022.09—2024.12</span>
    <span class="proj-title">某重点单位合作项目——AI 驱动超构表面（Metasurface）逆向设计与大模型框架</span>
    <span class="proj-role">主要负责人</span>
  </div>

  <p class="proj-para"><span class="proj-label">1. 研究目标：</span>针对超构表面（Metasurface）电磁响应设计依赖人工经验全波仿真、无法快速迭代的工程瓶颈，<b>首次提出</b>基于深度卷积变分自编码器（DCVAE）的结构-模式双向映射替代模型，将麦克斯韦方程组数值求解替换为毫秒级前向推理，正逆向速度均提升 <b>1000×</b>，同时构建行业领先的超构表面模式基因数据库。所构建的生成式替代模型框架在数学形式上与光学超表面建模同构，方法论可直接迁移至光学/近红外频段的超表面逆向设计任务。</p>

  <p class="proj-para"><span class="proj-label">2. 研究内容：</span>① 以棋盘式离散编码（12×12 网格）统一表征多样化超构表面结构，解决跨类型标准化建模难题。② 构建 <b>DCVAE</b> 替代模型：正向预测（结构→散射参数/RCS）和逆向设计（性能目标→最优结构）速度均提升至全波仿真的 <b>1000×</b>，满足实时参数化设计需求。③ 构建包含 <b>55,000 条</b>高质量超构表面特征模式样本的电磁数据库（超合同要求 10%），支撑大规模神经网络训练。④ 设计并制备物理样品，通过 CNAS 第三方认证测试，验证替代模型工程可用性。</p>

  <p class="proj-para"><span class="proj-label">3. 关键结果：</span><br>
  <b>DCVAE 替代模型：</b>正逆向推理速度均 <b>1000×</b> 于 HFSS/CST 全波仿真，数据压缩至 <b>0.012%</b>，空间分辨率 0.0072λ。<br>
  <b>数据库：</b>55,000 条超构表面 EM 数据，超合同 10%；RCS 调控幅度 <b>+193%</b>（合同要求 >20%）。<br>
  <b>工程交付：</b>物理样品通过 CNAS 认证测试；合同全部指标超额完成（速度 +900%，模式数量 +100%）。</p>

  <p class="proj-para"><span class="proj-label">4. 研究成果：</span>发表 <i>Microw. Opt. Technol. Lett.</i>（Wiley，已发表，唯一学生作者，Wiley 高被引作者奖 + Marina Forum 学生论文提名奖）；<i>ISAPE 2024</i>（已发表，第一作者）；<i>PIERS 2024</i>（已发表，受邀报告，唯一学生作者）。</p>
</div>
'''

# ── 项目三：华为（B版，Physics-Informed CMA + AI框架） ─────────────────────
PROJ3 = '''
<div class="proj-block">
  <div class="proj-header">
    <span class="proj-period">2023.09—2025.11</span>
    <span class="proj-title">华为横向合作项目——物理信息约束（Physics-Informed）驱动的 AI 天线设计框架</span>
    <span class="proj-role">主要负责人</span>
  </div>

  <p class="proj-para"><span class="proj-label">1. 研究目标：</span>针对纯数据驱动 AI 天线设计缺乏物理可解释性、搜索空间过大的核心缺陷，<b>首次提出</b>以特征模式分析（CMA）作为 Physics-Informed 约束嵌入 AI 优化框架，在设计早期锁定麦克斯韦方程组的物理可行域，将 PSO+ML 联合搜索的有效空间降低 <b>90%</b>，实现工程规格可达性的提前预判。</p>

  <p class="proj-para"><span class="proj-label">2. 研究内容：</span>① 以 CMA 精确提取天线结构的模式极限（Modal Significance 分布），建立"结构—模式—性能"的物理约束映射，排除麦克斯韦方程组物理不可达的设计方向。② 在物理可行域内部署 PSO + ML 联合优化，实现多目标（增益/带宽/方向图/隔离度）并行搜索；仅需 5-6 个低阶特征模式权重即可精确逼近目标方向图。③ 设计并验证 Tri-mode Fenced-Discone 天线（FDA）：覆盖 4.5–6 GHz，<b>28.6% 带宽</b>，≥<b>30 dB</b> 端口隔离，<b>7.4 dBi</b> 增益（θ=45°），支持天花板安装三模 MIMO AP。</p>

  <p class="proj-para"><span class="proj-label">3. 关键结果：</span><br>
  <b>Physics-Informed 框架：</b>CMA 约束将 AI 有效搜索空间降低 90%，避免物理不可行解；模式追踪精度优于传统 MAC 准则。<br>
  <b>工程指标：</b>FDA 天线 28.6% 带宽、≥30 dB 隔离、7.4 dBi 增益（θ=45°），实测效率 95%，圆极化圆度 ≤2 dB。<br>
  <b>交付：</b>完整理论框架交付华为产品线，为后续馈电优化提供物理约束基础。</p>

  <p class="proj-para"><span class="proj-label">4. 研究成果：</span>发表 <i>Electromagnetic Science</i>（IEEE 期刊，已发表，第一作者）；IEEE TAP 在写（草稿完成，唯一学生作者）；<i>IEEE APCAP 2024</i>（已发表，唯一学生作者）。</p>
</div>
'''

# ── 专业技能 ──────────────────────────────────────────────────────────────────
SKILLS = '''
<p class="skills-para"><b>精通 AI for Science 电磁仿真替代模型（Surrogate Modeling）研究范式：</b>
掌握多学科知识，技能储备包括（1）AI 方法：深度卷积变分自编码器（DCVAE/VAE）、物理信息神经网络（PINN / Physics-Informed Neural Networks）、生成式深度学习、神经算子（Neural Operators）、PSO / 遗传 / 代理模型优化算法；（2）电磁物理：麦克斯韦方程组全波求解、特征模式分析（CMA/CMT）、超构表面（Metasurface）电磁响应设计、矩量法、超构表面 RCS 调控；（3）仿真工具：<b>HFSS、CST Studio Suite</b>（博士论文核心仿真工具，深度使用，直接调用 API 开展分布式任务调度）。</p>
<p class="skills-para"><b>开源工程影响力（区别于课题组 Demo 的可复现验证）：</b>
GitHub 浏览量 <b>10 万+</b>，天线/超构表面 AI 设计领域排名第一；开源 ARIA AI 天线设计智能体（端到端电磁参数化设计推理引擎），Bilibili 演示视频破万播放，验证替代模型工程可用性；Wiley 高被引作者奖（2024）。</p>
<p class="skills-para"><b>优秀的数理基础与工程能力：</b>
擅于利用量化物理模型对电磁问题重新建模；具备微波暗室天线测试、PCB 设计与焊接、物理样品制备及 CNAS 第三方认证测试的完整工程交付能力；优秀的中英文沟通、写作能力，PIERS 受邀报告，Marina Forum 国际竞赛提名奖。</p>
'''

# ── 荣誉 ──────────────────────────────────────────────────────────────────────
HONORS = [
    ('01', 'Wiley 中国区高贡献作者奖（高被引）', 'Wiley 出版集团', '2024 · 国际'),
    ('02', '学生论文竞赛提名奖', '新加坡 Marina Forum 国际天线论坛（新加坡）', '2025 · 国际'),
    ('03', '美国大学生数学建模竞赛国际一等奖（MCM Meritorious）', '美国数学及其应用联合会', '2021 · 国际'),
    ('04', '全国大学生数学建模竞赛国家二等奖', '教育部', '2020 · 国家级'),
    ('05', '安徽恒信奖（全校当年仅授一人）', '安徽大学', '2022 · 校级最高荣誉'),
]

# ── 论文 ──────────────────────────────────────────────────────────────────────
PAPERS = [
    ('<b>Xi Chong You</b>, C.T. Gao, F.H. Lin, "Wideband Multi-Mode Tracking Using Near-Field Global-Correlation Method," '
     '<i>Electromagnetic Science</i>, vol.4, no.1, 0130512, Mar.2026.',
     'IEEE 期刊，Gold Open Access，第一作者'),
    ('<b>Xi Chong You</b>, F.H. Lin, "Inverse Design of Reflective Metasurface Antennas Using Deep Learning from Small-Scale Statistically Random Pico-Cells," '
     '<i>Microw. Opt. Technol. Lett.</i>, vol.66, no.2, pp.34068, Feb.2024.',
     'Wiley 已发表，唯一学生作者，Wiley 高被引作者奖 + Marina Forum 学生论文提名奖'),
    ('<b>Xi Chong You</b>, F.H. Lin, "Fast Design of Multi-Beam Metasurface Antennas Using Generative Machine Learning," '
     '<i>IEEE APCAP</i>, 南京, 2024.',
     '已发表，唯一学生作者'),
    ('<b>Xi Chong You</b>, F.H. Lin, "Energy Efficient Design of Low-Profile Wideband Microstrip Patch Antennas Using Deep Learning," '
     '<i>ICMMT</i>, 青岛, 2023.',
     '已发表，唯一学生作者，GitHub 领域首篇开源'),
    ('<b>Xi Chong You</b>, F.H. Lin, "Machine-learning Aided Design (MLAD) of Metasurfaces and Antennas," '
     '<i>PIERS</i>, 成都, 2024.',
     '已发表，受邀报告（Invited Talk），唯一学生作者'),
    ('<b>Xi Chong You</b>, F.H. Lin, "Tri-mode Fenced-Discone Antenna for Ceiling-Mounted MIMO AP," '
     '目标 <i>IEEE TAP</i>（在写）.',
     '唯一学生作者'),
    ('<b>Xi Chong You</b>, F.H. Lin, <i>IEEE iWAT 2026</i>, 英国, DOI: 10.1109/IWAT66946.2026.11501863.',
     '已发表，唯一学生作者'),
    ('C.T. Gao, <b>Xi Chong You</b>, F.H. Lin, "Significant Bandwidth Enhancement of Low-Reflection Checkerboard Metasurfaces," '
     '<i>ISAPE</i>, 合肥, 2024.',
     '已发表，第一学生作者'),
]

# ══════════════════════════════════════════════════════════════════════════════
# 生成网页版 HTML
# ══════════════════════════════════════════════════════════════════════════════
def make_honors_html(honors):
    rows = []
    for num, title, org, year in honors:
        rows.append(f'''
    <div class="honor-row">
      <span class="honor-num">{num}</span>
      <span class="honor-title">{title}</span>
      <span class="honor-org">{org}</span>
      <span class="honor-year">{year}</span>
    </div>''')
    return '\n'.join(rows)

def make_papers_html(papers):
    rows = []
    for i, (txt, note) in enumerate(papers, 1):
        rows.append(f'''
    <div class="paper-row">
      <span class="paper-num">[{i}]</span>
      <span class="paper-text">{txt}
        <span class="paper-badge">{note}</span>
      </span>
    </div>''')
    return '\n'.join(rows)

WEB_HTML = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>尤栖冲 · 简历 · AI电磁研究工程师（深圳消费电子）</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,600;1,400&family=JetBrains+Mono:wght@400;600&family=Noto+Serif+SC:wght@400;600;700&display=swap" rel="stylesheet">
<style>
:root{{
  --ink:     #0D1B2A;
  --ink2:    #3A4A5C;
  --ink3:    #6B7A8D;
  --blue:    #1A3A6B;
  --gold:    #A87C2A;
  --gold-lt: #D4AA5A;
  --line:    #D8DDE5;
  --bg:      #F8F7F4;
  --white:   #FFFFFF;
}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:var(--bg);font-family:'Noto Serif SC',serif;color:var(--ink);font-size:14px;line-height:1.75}}
.page{{max-width:860px;margin:32px auto;background:var(--white);padding:40px 48px;
       box-shadow:0 2px 24px rgba(0,0,0,.10);
       border-left:4px solid;
       border-image:linear-gradient(180deg,var(--blue),var(--gold)) 1}}
/* ─ 页眉 ─ */
.header-wrap{{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:24px}}
.header-photo img{{width:80px;height:106px;border-radius:2px;object-fit:cover}}
.name{{font-size:26px;font-weight:700;color:var(--blue);letter-spacing:.05em}}
.name-sub{{font-size:13px;color:var(--ink3);margin-left:8px}}
.job-intent{{margin:6px 0 4px;font-size:13px}}
.job-intent .label{{color:var(--ink3)}}
.job-intent .value{{color:var(--blue);font-weight:600}}
.info-line{{font-size:12px;color:var(--ink3);margin-top:2px;font-family:'JetBrains Mono',monospace}}
/* ─ 节标题 ─ */
.sec-title{{font-size:13px;font-weight:700;color:var(--blue);letter-spacing:.25em;text-transform:uppercase;
            margin:28px 0 12px;position:relative;padding-bottom:6px}}
.sec-title::after{{content:'';position:absolute;bottom:0;left:0;right:0;height:1px;
                    background:linear-gradient(90deg,var(--blue) 0%,var(--line) 100%)}}
/* ─ 教育 ─ */
.edu-table{{width:100%;border-collapse:collapse}}
.edu-table td{{padding:4px 8px 4px 0;vertical-align:top}}
.edu-year{{color:var(--ink3);font-family:'JetBrains Mono',monospace;font-size:12px;white-space:nowrap;width:180px}}
.edu-school{{color:var(--ink);font-size:13.5px}}
.edu-rank{{color:var(--blue);font-size:12.5px;font-weight:600;text-align:right;white-space:nowrap}}
.edu-note{{font-size:12px;color:var(--ink3);margin-top:6px}}
/* ─ 项目 ─ */
.proj-block{{margin-bottom:22px}}
.proj-header{{display:flex;align-items:baseline;flex-wrap:wrap;gap:8px;
              background:rgba(26,58,107,.05);border-top:2px solid var(--blue);
              padding:6px 10px;margin-bottom:8px}}
.proj-period{{font-family:'JetBrains Mono',monospace;font-size:11.5px;color:var(--ink3);white-space:nowrap}}
.proj-title{{font-weight:700;color:var(--blue);font-size:14px;flex:1}}
.proj-role{{font-size:11.5px;color:var(--gold);white-space:nowrap}}
.proj-para{{font-size:13px;color:var(--ink2);margin-bottom:6px;text-align:justify}}
.proj-label{{font-weight:700;color:var(--ink)}}
/* ─ 技能 ─ */
.skills-para{{font-size:13px;color:var(--ink2);margin-bottom:8px;text-align:justify}}
/* ─ 荣誉 ─ */
.honor-row{{display:flex;align-items:baseline;gap:12px;margin-bottom:6px;font-size:13px}}
.honor-num{{font-family:'JetBrains Mono',monospace;color:var(--gold);font-weight:600;font-size:11px;width:22px;flex-shrink:0}}
.honor-title{{color:var(--ink);flex:1;font-weight:600}}
.honor-org{{color:var(--ink3);font-size:12px}}
.honor-year{{color:var(--blue);font-size:12px;white-space:nowrap}}
/* ─ 论文 ─ */
.paper-row{{display:flex;gap:8px;margin-bottom:8px;font-size:12.5px;color:var(--ink2)}}
.paper-num{{font-family:'JetBrains Mono',monospace;color:var(--ink3);flex-shrink:0;padding-top:2px}}
.paper-text{{flex:1;text-align:justify}}
.paper-badge{{display:inline-block;background:#C62828;color:#fff;font-size:10.5px;
               padding:1px 6px;border-radius:2px;margin-left:6px;vertical-align:middle;font-family:'JetBrains Mono',monospace}}
</style>
</head>
<body>
<div class="page">

<!-- ══ 页眉 ══════════════════════════════════════════════════════ -->
<div class="header-wrap">
  <div class="header-left">
    <div class="name-line">
      <span class="name">尤栖冲</span>
      <span class="name-sub">（在读博士·2027届）</span>
    </div>
    <div class="job-intent">
      <span class="label">求职意向：</span>
      <span class="value">{INTENT}</span>
    </div>
    <div class="info-line">出生年月：2000.08 &nbsp;&nbsp; 联系电话：15365972193 &nbsp;&nbsp; 政治面貌：中共党员</div>
    <div class="info-line">邮箱：youxch2022@shanghaitech.edu.cn &nbsp;&nbsp; GitHub：github.com/youxch</div>
  </div>
  <div class="header-photo">
    <img src="data:image/png;base64,{PHOTO_B64}" alt="photo">
  </div>
</div>

<!-- ══ 科研项目 ══════════════════════════════════════════════════ -->
<div class="sec-title">科研项目</div>
{PROJ1}
{PROJ2}
{PROJ3}

<!-- ══ 教育背景 ══════════════════════════════════════════════════ -->
<div class="sec-title">教育背景</div>
<table class="edu-table">
{EDU}
</table>
<div class="edu-note">{EDU_NOTE}</div>

<!-- ══ 专业技能 ══════════════════════════════════════════════════ -->
<div class="sec-title">专业技能</div>
{SKILLS}

<!-- ══ 个人荣誉 ══════════════════════════════════════════════════ -->
<div class="sec-title">个人荣誉</div>
{make_honors_html(HONORS)}

<!-- ══ 发表论文 ══════════════════════════════════════════════════ -->
<div class="sec-title">发表论文</div>
{make_papers_html(PAPERS)}

</div>
</body>
</html>'''

# ══════════════════════════════════════════════════════════════════════════════
# 生成打印版（复用现有打印版CSS，只替换 body 内容）
# ══════════════════════════════════════════════════════════════════════════════
# 从现有打印版提取 <body> 之前的 CSS head，替换 body 部分

body_content_print = f'''<body>

<div class="page">

<!-- ══ 页眉 ══════════════════════════════════════════════════════ -->
<div class="header-wrap">
  <div class="header-left">
    <div class="name-line">
      <span class="name">尤栖冲</span>
      <span class="name-sub">（在读博士·2027届）</span>
    </div>
    <div class="job-intent">
      <span class="label">求职意向：</span>
      <span class="value">{INTENT}</span>
    </div>
    <div class="info-line">出生年月：2000.08 &nbsp;&nbsp; 联系电话：15365972193 &nbsp;&nbsp; 政治面貌：中共党员</div>
    <div class="info-line">邮箱：youxch2022@shanghaitech.edu.cn &nbsp;&nbsp; GitHub：github.com/youxch</div>
  </div>
</div>

<!-- ══ 教育背景 ══════════════════════════════════════════════════ -->
<div class="sec-title">教育背景</div>
<table class="edu-table">
{EDU}
</table>
<div class="edu-note">{EDU_NOTE}</div>

<!-- ══ 科研项目 ══════════════════════════════════════════════════ -->
<div class="sec-title">科研项目</div>
{PROJ1}
{PROJ2}
{PROJ3}

<!-- ══ 专业技能 ══════════════════════════════════════════════════ -->
<div class="sec-title">专业技能</div>
{SKILLS}

<!-- ══ 个人荣誉 ══════════════════════════════════════════════════ -->
<div class="sec-title">个人荣誉</div>
{make_honors_html(HONORS)}

<!-- ══ 发表论文 ══════════════════════════════════════════════════ -->
<div class="sec-title">发表论文</div>
{make_papers_html(PAPERS)}

</div>
</body>
</html>'''

body_start = PRINT_TEMPLATE.index('<body>')
PRINT_HTML = PRINT_HEAD + '\n' + body_content_print

# ══════════════════════════════════════════════════════════════════════════════
# 生成文字参考稿（纯文字）
# ══════════════════════════════════════════════════════════════════════════════
import re as _re

def strip_tags(s):
    return _re.sub(r'<[^>]+>', '', s).strip()

def paper_plain(papers):
    lines = []
    for i,(txt,note) in enumerate(papers,1):
        lines.append(f'[{i}] {strip_tags(txt)}（{note}）')
    return '\n'.join(lines)

def honor_plain(honors):
    lines = []
    for num,title,org,year in honors:
        lines.append(f'{num}. {title} — {org}（{year}）')
    return '\n'.join(lines)

REF_BODY = f'''
求职意向：{strip_tags(INTENT)}

═══ 科研项目 ═══

{strip_tags(PROJ1.replace('<br>','\\n'))}

{strip_tags(PROJ2.replace('<br>','\\n'))}

{strip_tags(PROJ3.replace('<br>','\\n'))}

═══ 教育背景 ═══
2022.09—2027.07  上海科技大学（双一流） 电子科学与技术 硕博连读  成绩前1%
2018.09—2022.06  安徽大学（211双一流） 电子信息工程 工学学士   3/123（保研推免）
{EDU_NOTE}

═══ 专业技能 ═══
{strip_tags(SKILLS.replace('<br>','\\n'))}

═══ 个人荣誉 ═══
{honor_plain(HONORS)}

═══ 发表论文 ═══
{paper_plain(PAPERS)}
'''

REF_HTML = f'''<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="UTF-8">
<title>内容参考稿 · AI电磁方向 · 深圳消费电子</title>
<style>body{{font-family:sans-serif;max-width:800px;margin:32px auto;font-size:14px;line-height:1.8;white-space:pre-wrap;}}</style>
</head><body>{REF_BODY}</body></html>'''

# ══════════════════════════════════════════════════════════════════════════════
# 输出文件
# ══════════════════════════════════════════════════════════════════════════════
forbidden = ['RGB三色法', 'CLIP多模态', '合同金额', '国防科技大学', 'NUDT',
             '68.5', 'TAP，已接受', 'TAP accept', 'TAP接受']

files = {
    '尤栖冲_深圳消费电子_AI电磁方向.html': PRINT_HTML,
    '尤栖冲_深圳消费电子_AI电磁方向_网页版.html': WEB_HTML,
    '内容参考_AI电磁方向_深圳消费电子.html': REF_HTML,
}

for fname, content in files.items():
    path = os.path.join(OUT_DIR, fname)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    size_kb = len(content.encode('utf-8')) // 1024
    print(f'OK  {fname}  ({size_kb} KB)')

# 禁用词检查
all_content = ' '.join(files.values())
found = [w for w in forbidden if w in all_content]
if found:
    print(f'FAIL 禁用词: {found}')
else:
    print('PASS 所有文件：no forbidden terms')
