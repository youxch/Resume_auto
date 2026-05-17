#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('d:/YXC/YXC_know/Resume/简历/尤栖冲_华为诺亚_B方向.html', encoding='utf-8') as f:
    template = f.read()

body_start = template.index('<body>')
head_part = template[:body_start]

# Update title
head_part = head_part.replace(
    '尤栖冲 · 简历 · 华为诺亚方舟 B方向',
    '尤栖冲 · 简历 · Ansys中国 混合方向'
)

photo_start = template.index('<img src="data:image/png;base64,')
img_tag_end = template.index('>', photo_start) + 1
img_tag = template[photo_start:img_tag_end]

new_body = '''<body>

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
      <span class="value">仿真应用工程师（AI/ML 方向）&nbsp;·&nbsp; 电磁仿真算法研究员</span>
    </div>
    <div class="info-line">出生年月：2000.08 &nbsp;&nbsp; 联系电话：15365972193 &nbsp;&nbsp; 政治面貌：中共党员</div>
    <div class="info-line">邮箱：youxch2022@shanghaitech.edu.cn &nbsp;&nbsp; GitHub：github.com/youxch</div>
  </div>
  <div class="header-photo">
    ''' + img_tag + '''
  </div>
</div>

<!-- ══ 教育背景 ══════════════════════════════════════════════════ -->
<div class="sec-title">教育背景</div>
<table class="edu-table">
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
</table>
<div class="edu-note">博士主修：深度学习、高阶分布式系统、天线理论与技术、矩阵计算 &nbsp;&nbsp; 导师：林丰涵 教授</div>

<!-- ══ 科研项目 ══════════════════════════════════════════════════ -->
<div class="sec-title">科研项目</div>

<!-- 项目一：NSFC — AI加速仿真框架（混合方向主打） -->
<div class="proj-block">
  <div class="proj-header">
    <span class="proj-period">2024.09—至今</span>
    <span class="proj-title">国家自然科学基金面上项目——AI for Science 电磁仿真加速平台</span>
    <span class="proj-role">主要负责人（博士生主导）</span>
  </div>

  <p class="proj-para"><span class="proj-label">1. 研究目标：</span>针对 HFSS/CST 全波仿真耗时数小时至数天、百万级训练集工程上不可行的根本瓶颈，<b>首次提出</b>从并行仿真基础设施到生成式逆向设计引擎的完整 AI 加速链路，将天线/超构表面全波仿真加速 <b>5000×</b>，同时将所需数据规模降至 <b>0.012%</b>，实现从"数据不可能"到"设计秒级完成"的全链路突破。</p>

  <p class="proj-para"><span class="proj-label">2. 研究内容：</span>① 搭建<b>行业首个</b>数百台服务器并行仿真系统（直接调用 HFSS/CST API 进行分布式仿真任务调度），效率相比单机仿真提升 <b>300×</b>，将百万级仿真数据集从不可行变为可行。② <b>首次提出</b>无需物理先验知识的统计分布随机筛选法：所需数据规模降至原有的 <b>0.012%</b>，仿真成本降低 99%；开源后 GitHub 浏览量突破 <b>10 万</b>，天线/超构表面领域排名第一。③ 构建天线专用变分自编码器（VAE）逆向设计引擎：结构↔性能双向映射，逆向设计时间缩至 <b>1 秒</b>（比 HFSS/CST 仿真快 <b>5000×</b>），大型超构表面设计从数周缩至 <b>5 分钟</b>。④ 突破低剖面天线增益带宽极限：CMA 物理先验指导 + ML 优化联合作用，增益带宽提升 <b>20%</b>，超越现有文献最优。</p>

  <p class="proj-para"><span class="proj-label">3. 关键结果：</span><br>
  <b>仿真加速基础设施：</b>行业首个百台级并行仿真系统，<b>300×</b> 加速，直接兼容 HFSS/CST API，可扩展至任意全波仿真器。<br>
  <b>数据效率：</b>所需数据 <b>0.012%</b>，仿真成本降低 99%；GitHub 开源 <b>10 万+</b> 浏览，验证方法可复现。<br>
  <b>设计效率：</b>逆向设计 <b>1 秒</b>（比 HFSS/CST 快 <b>5000×</b>），超构表面设计从数周缩至 <b>5 分钟</b>。<br>
  <b>性能突破：</b>增益带宽提升 <b>20%</b>，超越文献最优。ARIA 天线 AI 设计智能体（Bilibili 演示破万播放）。</p>

  <p class="proj-para"><span class="proj-label">4. 研究成果：</span>发表 <i>Electromagnetic Science</i>（IEEE 期刊，Gold Open Access，已发表，第一作者）；<i>IEEE iWAT 2026</i>（已发表，唯一学生作者）；<i>ICMMT 2023</i>（已发表，唯一学生作者，GitHub 领域首篇开源）；<i>IEEE APCAP 2024</i>（已发表，唯一学生作者）。</p>
</div>

<!-- 项目二：重点单位合作 — DCVAE 数据库与逆向设计 -->
<div class="proj-block">
  <div class="proj-header">
    <span class="proj-period">2022.09—2024.12</span>
    <span class="proj-title">某重点单位合作项目——AI 驱动超构表面模式基因提取与逆向设计</span>
    <span class="proj-role">主要负责人</span>
  </div>

  <p class="proj-para"><span class="proj-label">1. 研究目标：</span>针对超构表面全波仿真极慢（单次数小时至数天）、AI 设计缺乏高质量数据集、正逆向映射精度不足的三重瓶颈，<b>首次提出</b>深度卷积变分自编码器（DCVAE）驱动的"模式基因"提取与编辑框架，在<b>行业首个</b> 55,000 条超构表面特征模式数据库支撑下，构建结构↔模式双向映射引擎，正逆向速度均达全波仿真 <b>1000×</b>。</p>

  <p class="proj-para"><span class="proj-label">2. 研究内容：</span>① 提出棋盘式离散编码（12×12 网格）统一表征超构表面结构，解决 HFSS/CST 全波仿真与 AI 模型之间的数据接口标准化问题。② 构建 DCVAE 生成式模型：正向预测（给结构→算性能）和逆向设计（给性能→找结构）均达全波仿真 <b>1000×</b>。③ 构建行业首个 55,000 条超构表面特征模式高质量数据库，所有数据均通过 HFSS/CST 全波仿真生成，空间分辨率 <b>0.0072λ</b>（优于行业基准 0.01λ 达 28%）。④ 制备物理样品并通过 CNAS 第三方认证测试，验证 AI 设计结果的工程可行性。</p>

  <p class="proj-para"><span class="proj-label">3. 关键结果：</span><br>
  <b>生成模型性能：</b>DCVAE 正逆向速度均达全波仿真 <b>1000×</b>，支持当天完成多轮设计迭代（传统方法需数天/数周）。<br>
  <b>数据库规模：</b>55,000 条，行业领先，空间分辨率 <b>0.0072λ</b>，超出行业基准 28%。<br>
  <b>RCS 工程验证：</b>RCS 变化幅度 <b>+193%</b>，物理样品通过 CNAS 第三方认证测试。</p>

  <p class="proj-para"><span class="proj-label">4. 研究成果：</span>发表 <i>Microw. Opt. Technol. Lett.</i>（Wiley，已发表，唯一学生作者，Wiley 高被引作者奖 + Marina Forum（新加坡）学生论文提名奖）；<i>ISAPE 2024</i>（已发表，第一作者）。</p>
</div>

<!-- 项目三：华为 — 物理约束驱动方法论 -->
<div class="proj-block">
  <div class="proj-header">
    <span class="proj-period">2023.09—2025.11</span>
    <span class="proj-title">华为横向合作项目——物理约束驱动的 AI 天线设计方法论</span>
    <span class="proj-role">主要负责人</span>
  </div>

  <p class="proj-para"><span class="proj-label">1. 研究目标：</span>针对 AI 天线设计常被批评为"黑盒"、缺乏物理可解释性的核心痛点，<b>首次提出</b> CMA 基函数加权可行性论证方法，将特征模式分析（CMA）从定性指导工具升级为定量约束框架，在天线设计前通过 CMA + PSO 联合优化确定设计可行域，实现"物理先验-AI 优化-工程交付"的完整闭环。</p>

  <p class="proj-para"><span class="proj-label">2. 研究内容：</span>① <b>首次提出</b> CMA 基函数加权可行性论证方法：以 CMA 特征模式为基函数，PSO 优化模式权重，定量论证目标方向图物理可实现性（揭示色散效应为宽带高抑制波束核心瓶颈），将"先仿真后判断"变为"先约束后设计"。② 提出三模式接力谐振天线（FDA），三模接力实现 <b>28.6%</b> 阻抗带宽（传统方法约 10%），验证物理约束驱动 AI 设计的有效性。③ <b>首次提出</b>"消除激励源"互耦抑制新思想：区别于文献"消除散射源"路线，纯物理机制实现全频段 MIMO 隔离 <b>≥30 dB</b>，无需任何 AI 优化额外引入的去耦结构。④ 制备物理样机（铝合金+黄铜+3D打印治具），微波暗室全参数实测验证。</p>

  <p class="proj-para"><span class="proj-label">3. 关键结果：</span><br>
  <b>可行性论证：</b>CMA 定量论证将仿真前判断从"不可能"变为"精确可行域"，设计迭代周期大幅缩短。<br>
  <b>性能验证：</b>带宽 <b>28.6%</b>、隔离 <b>≥30 dB</b>（全频段，无额外结构）、增益 7.4 dBi（θ=45°）、效率 95%，超越 NUS 2022/2024/2025 三篇同类工作。<br>
  <b>方法论价值：</b>物理约束（CMA）→ AI 优化（PSO/ML）→ 工程交付（CNAS 级样机）完整链路，为 Ansys SimAI 等 AI 仿真加速工具提供物理先验嵌入的参考范式。</p>

  <p class="proj-para"><span class="proj-label">4. 研究成果：</span>发表 <i>IEEE iWAT 2026</i>（已发表，唯一学生作者）；FDA 天线论文草稿完成，目标投稿 <i>IEEE Trans. Antennas Propag.</i>（唯一学生作者）。</p>
</div>

<!-- ══ 专业技能 ══════════════════════════════════════════════════ -->
<div class="sec-title">专业技能</div>
<div class="skill-block">
  <p><b>深度使用 HFSS 与 CST 全波仿真（博士论文核心工具）：</b>长期使用 HFSS、CST Studio 进行天线/超构表面全波电磁仿真（含 API 批量调用）；精通特征模式分析（CMA）；同时开发了基于深度学习的仿真加速框架，实现比 HFSS/CST 单次仿真快 <b>5000×</b> 的逆向设计引擎——深度理解仿真工具的工程边界与 AI 加速的正确落地场景。</p>
  <p><b>精通 AI4S 仿真加速方法论：</b>技能储备包括（1）变分自编码器（VAE）、深度卷积变分自编码器（DCVAE）生成模型，实现结构↔性能双向逆向映射；（2）搭建数百台服务器并行仿真基础设施（行业首创，300× 加速，兼容 HFSS/CST API）；（3）PSO/遗传/代理模型优化算法结合 CMA 物理约束，构建"物理可解释"AI 优化框架。</p>
  <p><b>开源影响力（可验证，非课题组内部 demo）：</b>GitHub 浏览量 <b>10 万+</b>，天线/超构表面领域排名第一；开发 ARIA 天线 AI 设计智能体（GitHub 开源 + Bilibili 演示破万播放）；逆向设计系列开源工具已成为领域标杆参考，证明方法真实可用。</p>
  <p><b>硬件与工程能力：</b>具备从仿真到实物全链路工程能力：PCB 设计与焊接、STM32 嵌入式开发、毫米波雷达调试、铝合金/黄铜样机制备（含 3D 打印治具）；物理样机均经微波暗室实测，两项成果通过 CNAS 第三方认证，仿真与实测高度吻合。</p>
  <p><b>编程与数理基础：</b>Python（主力，含仿真 API 自动化脚本）、MATLAB、C；扎实的优化理论与概率统计基础；优秀的中英文沟通与写作能力，国际会议报告及获奖经验（PIERS 2024 受邀报告）。</p>
</div>

<!-- ══ 个人荣誉 ══════════════════════════════════════════════════ -->
<div class="sec-title">个人荣誉</div>
<ul class="honor-list">
  <li><b>Wiley 中国区高贡献作者奖（高被引）</b> — Wiley 出版集团，2024 年，国际级</li>
  <li><b>学生论文竞赛提名奖</b> — 新加坡 Marina Forum（新加坡）国际天线论坛，2025 年，国际级</li>
  <li><b>美国大学生数学建模竞赛国际一等奖（MCM Meritorious）</b> — 美国数学及其应用联合会，2021 年</li>
  <li><b>全国大学生数学建模竞赛国家二等奖</b> — 教育部，2020 年</li>
  <li><b>安徽恒信奖（全校当年仅授一人）</b> — 安徽大学，2022 年，校级最高荣誉</li>
  <li><b>上海科技大学学业奖学金</b> — 连续两年（2023–2025）</li>
  <li><b>MathorCup 数学建模竞赛国家三等奖</b> — 中国运筹学会，2023 年</li>
</ul>

<!-- ══ 发表论文 ══════════════════════════════════════════════════ -->
<div class="sec-title">发表论文（共 8 篇，含 1 篇在写；按与仿真+AI 方向相关性排序）</div>
<ol class="paper-list">
  <li>
    <b>Xi Chong You</b>, C.T. Gao, F.H. Lin, "Wideband Multi-Mode Tracking Using Near-Field Global-Correlation Method," <i>Electromagnetic Science</i>, vol. 4, no. 1, 0130512, Mar. 2026.
    <span class="paper-note">（IEEE 期刊，Gold Open Access，第一作者）</span>
  </li>
  <li>
    <b>Xi Chong You</b>, F.H. Lin, "Inverse Design of Reflective Metasurface Antennas Using Deep Learning from Small-Scale Statistically Random Pico-Cells," <i>Microw. Opt. Technol. Lett.</i>, vol. 66, no. 2, pp. 34068, Feb. 2024.
    <span class="paper-note">（Wiley，已发表，第一作者，唯一学生作者，Wiley 高被引作者奖 + Marina Forum（新加坡）学生论文提名奖）</span>
  </li>
  <li>
    <b>Xi Chong You</b>, F.H. Lin, "Energy Efficient Design of Low-Profile Wideband Microstrip Patch Antennas Using Deep Learning," <i>ICMMT 2023</i>, Qingdao.
    <span class="paper-note">（已发表，第一作者，唯一学生作者，GitHub 领域首篇开源、浏览量最高）</span>
  </li>
  <li>
    <b>Xi Chong You</b>, F.H. Lin, "Fast Design of Multi-Beam Metasurface Antennas Using Generative Machine Learning," <i>IEEE APCAP 2024</i>, Nanjing.
    <span class="paper-note">（已发表，第一作者，唯一学生作者）</span>
  </li>
  <li>
    <b>Xi Chong You</b>, F.H. Lin, "Machine-learning Aided Design (MLAD) of Metasurfaces and Antennas," <i>PIERS 2024</i>, Chengdu.
    <span class="paper-note">（受邀报告 Invited Talk，已发表，第一作者，唯一学生作者）</span>
  </li>
  <li>
    <b>Xi Chong You</b>, F.H. Lin, "Wideband Massive Characteristic-Mode Tracking of Metasurfaces Using Single-Layer Near-Field Global-Correlation (NFGC) Method," <i>2026 IEEE International Workshop on Antenna Technology (iWAT)</i>, DOI: 10.1109/IWAT66946.2026.11501863.
    <span class="paper-note">（IEEE 国际天线技术研讨会，已发表，第一作者，唯一学生作者）</span>
  </li>
  <li>
    <b>Xi Chong You</b>, F.H. Lin, "Tri-mode Fenced-Discone Antenna (FDA) for Ceiling-Mounted MIMO AP," target: <i>IEEE Trans. Antennas Propag.</i>, manuscript in preparation.
    <span class="paper-note">（IEEE TAP，目标投稿，第一作者，唯一学生作者）</span>
  </li>
  <li>
    <b>Xi Chong You</b>, C.T. Gao, F.H. Lin, "Significant Bandwidth Enhancement of Low-Reflection Checkerboard Metasurfaces Using Machine Learning," <i>ISAPE 2024</i>, Hefei.
    <span class="paper-note">（已发表，第一作者）</span>
  </li>
</ol>

</div><!-- end .page -->
</body>
</html>'''

output = head_part + new_body

with open('d:/YXC/YXC_know/Resume/简历/尤栖冲_Ansys中国_混合方向.html', 'w', encoding='utf-8') as f:
    f.write(output)

print(f"Done! {len(output)} bytes written.")
