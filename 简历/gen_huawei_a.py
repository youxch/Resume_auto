#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('d:/YXC/YXC_know/Resume/简历/尤栖冲_华为诺亚_B方向.html', encoding='utf-8') as f:
    template = f.read()

body_start = template.index('<body>')
head_part = template[:body_start]

# Extract photo img tag
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
      <span class="value">天线/电磁算法研究员 &nbsp;·&nbsp; 射频系统研究员</span>
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

<!-- 项目一：华为 -->
<div class="proj-block">
  <div class="proj-header">
    <span class="proj-period">2023.09—2025.11</span>
    <span class="proj-title">华为横向合作项目——三模宽带全向天线与MIMO阵列设计</span>
    <span class="proj-role">主要负责人</span>
  </div>

  <p class="proj-para"><span class="proj-label">1. 研究目标：</span>针对吸顶式 WiFi AP 天线需同时满足宽频段（5.15–5.85 GHz）、高隔离（MIMO ≥30 dB）、全向波束（圆度 ≤2 dB）三项相互冲突约束、传统逐点仿真需数周且缺乏可行性先验判断的工程瓶颈，<b>首次提出</b> CMA 基函数加权可行性论证方法 + 三模式接力谐振设计范式，在无任何额外去耦结构的条件下实现三项指标全部超出华为规格要求。</p>

  <p class="proj-para"><span class="proj-label">2. 研究内容：</span>① <b>首次提出</b> CMA 基函数加权可行性论证方法：在通用阻抗表面上提取特征模式作为基函数，以 PSO 优化模式权重，定量论证目标方向图的物理可实现性，揭示色散效应是宽带高抑制波束的核心瓶颈（仅需 3–4 个模式即可描述，2 个不足，3 个 MSE≈207 可接受），为设计提供物理先验指导。② 提出三模式接力谐振天线（Tri-mode Fenced-Discone，FDA）：栅栏模式 J1（3–5 GHz）控制方向图"收腰"、盘锥模式 J2（3.5–6 GHz）承载中频辐射、短路片模式 J3（5–9 GHz）拓展高频覆盖，三模接力实现带宽 <b>28.6%</b>（4.5–6 GHz），对照组（无栅栏）仅约 10%。③ <b>首次提出</b>"消除激励源"互耦抑制新思想：区别于文献主流"消除散射源"路线（NUS 2018），倾斜栅栏柱子产生反相电流，阻止地板表面电流传播至相邻单元，全频段端口隔离 <b>≥30 dB</b>，无需任何额外去耦结构或网络。④ 制备铝6061车铣+镀镍盘锥/黄铜棒栅栏/3D打印焊接治具的物理样机，于微波暗室完成全参数实测验证。</p>

  <p class="proj-para"><span class="proj-label">3. 关键结果：</span></p>
  <table class="result-table">
    <tr><th>指标</th><th>华为规格要求</th><th>实测结果</th></tr>
    <tr><td>工作带宽</td><td>5.15–5.85 GHz</td><td><b>4.5–6 GHz（28.6%）</b></td></tr>
    <tr><td>θ=45° 增益</td><td>4–6 dBi</td><td><b>7.4 dBi（超出规格）</b></td></tr>
    <tr><td>方向图圆度</td><td>≤2 dB</td><td><b>≤2 dB（θ=30°–50°）</b></td></tr>
    <tr><td>端口隔离（2×2 MIMO）</td><td>≥30 dB</td><td><b>≥30 dB 全频段，无额外结构</b></td></tr>
    <tr><td>总辐射效率</td><td>—</td><td><b>95%</b></td></tr>
  </table>
  <p class="proj-result-note">对标 NUS 2022/2024/2025 三篇同类工作：本方案无需任何外部补偿结构，带宽 <b>28.6%</b> 为同类最宽、隔离 <b>≥30 dB</b> 全频段为同类最高，NUS 各篇均需额外去耦结构且指标不及本方案。</p>

  <p class="proj-para"><span class="proj-label">4. 研究成果：</span>发表 <i>IEEE iWAT 2026</i>（英国IEEE年会，已发表，唯一学生作者）；FDA 天线论文草稿完成，目标投稿 <i>IEEE Trans. Antennas Propag.</i>（唯一学生作者）。</p>
</div>

<!-- 项目二：重点单位合作 -->
<div class="proj-block">
  <div class="proj-header">
    <span class="proj-period">2022.09—2024.12</span>
    <span class="proj-title">某重点单位合作项目——超构表面 RCS 调控与模式基因编辑</span>
    <span class="proj-role">主要负责人</span>
  </div>

  <p class="proj-para"><span class="proj-label">1. 研究目标：</span>针对超构表面电磁性能设计依赖全波仿真（单次数小时至数天）、设计师高度依赖经验且缺乏系统化调控手段的工程瓶颈，<b>首次提出</b>深度卷积变分自编码器（DCVAE）驱动的"模式基因"提取与编辑方法，构建结构↔模式双向映射引擎，正逆向速度均提升至全波仿真的 <b>1000×</b>，实现可量化、可编辑的电磁模式精准操控。</p>

  <p class="proj-para"><span class="proj-label">2. 研究内容：</span>① 提出棋盘式离散编码（12×12 网格）统一表征超构表面结构，解决多样化结构的标准化建模难题。② 构建 DCVAE 模式基因双向映射引擎：正向预测（给结构→算性能）速度达全波仿真 <b>1000×</b>；逆向设计（给性能→找结构）同样达 <b>1000×</b>，支持当天完成多轮设计迭代。③ 构建 55,000 条超构表面特征模式高质量数据库（超合同要求 10%），空间分辨率达 <b>0.0072λ</b>（优于合同要求 0.01λ 达 28%）。④ 制备物理样品并通过 CNAS 第三方认证测试，具备独立可验证的工程交付能力。</p>

  <p class="proj-para"><span class="proj-label">3. 关键结果：</span><br>
  <b>模式调控：</b>模式抑制 2 个（显著性 >50%，超合同要求 <b>100%</b>）；新增模式 2 个（超合同要求 <b>100%</b>）。<br>
  <b>RCS 调控：</b>RCS 变化幅度 <b>+193%</b>（超合同要求 873%），频率可调范围提升 <b>22%</b>。<br>
  <b>速度突破：</b>正逆向均达全波仿真 <b>1000×</b>（超合同要求 900%）；空间分辨率 <b>0.0072λ</b>，超出合同要求 28%。<br>
  <b>工程交付：</b>全部合同指标超额完成，物理样品通过 CNAS 第三方认证测试。</p>

  <p class="proj-para"><span class="proj-label">4. 研究成果：</span>发表 <i>Microw. Opt. Technol. Lett.</i>（Wiley，已发表，唯一学生作者，Wiley 高被引作者奖 + Marina Forum（新加坡）学生论文提名奖）；<i>ISAPE 2024</i>（合肥，已发表，第一作者）。</p>
</div>

<!-- 项目三：NSFC -->
<div class="proj-block">
  <div class="proj-header">
    <span class="proj-period">2024.09—至今</span>
    <span class="proj-title">国家自然科学基金面上项目——AI 辅助宽带天线与超构表面设计</span>
    <span class="proj-role">主要负责人（博士生主导）</span>
  </div>

  <p class="proj-para"><span class="proj-label">1. 研究目标：</span>针对天线 AI 设计的数据瓶颈——高质量仿真数据生成极慢（单条需数小时）、百万级训练集工程上不可行——<b>首次提出</b>从数据生成基础设施到逆向设计引擎的完整 AI 加速链路，实现增益带宽性能突破 <b>20%</b>、超越现有文献最优结果，并将设计周期从数周缩短至 <b>1 秒</b>。</p>

  <p class="proj-para"><span class="proj-label">2. 研究内容：</span>① 搭建<b>行业首个</b>数百台服务器并行仿真系统，效率相比单机仿真提升 <b>300×</b>，将百万级数据集从不可行变为可行。② <b>首次提出</b>无需物理先验知识的统计分布随机筛选法：数据规模降至原有的 <b>0.012%</b>，仿真成本降低 99%；开源后 GitHub 浏览量突破 <b>10 万</b>，天线/超构表面领域排名第一。③ 构建天线专用 VAE 逆向设计引擎：逆向设计时间缩至 <b>1 秒</b>（比传统仿真快 <b>5000×</b>），大型超构表面设计从数周缩至 <b>5 分钟</b>。④ 突破低剖面天线增益带宽极限：CMA 物理先验指导 + ML 优化联合作用，增益带宽提升 <b>20%</b>，超越文献最优。</p>

  <p class="proj-para"><span class="proj-label">3. 关键结果：</span><br>
  <b>近场全局相关多模追踪：</b>首次提出 NFGC 方法，实现宽带超构表面海量特征模式无歧义追踪，发表于 <i>Electromagnetic Science</i>（IEEE 期刊，Gold Open Access，vol.4, no.1, Mar.2026）。<br>
  <b>设计效率：</b>并行 300×、数据 0.012%、逆向设计 1 秒；开源 GitHub 10万+ 浏览验证可落地。<br>
  <b>性能突破：</b>增益带宽提升 20%，超越现有文献最优。</p>

  <p class="proj-para"><span class="proj-label">4. 研究成果：</span>发表 <i>Electromagnetic Science</i>（IEEE 期刊，已发表，第一作者）；<i>IEEE iWAT 2026</i>（已发表，唯一学生作者）；<i>ICMMT 2023</i>（已发表，唯一学生作者，GitHub 领域首篇开源）；<i>IEEE APCAP 2024</i>（已发表，唯一学生作者）。</p>
</div>

<!-- ══ 专业技能 ══════════════════════════════════════════════════ -->
<div class="sec-title">专业技能</div>
<div class="skill-block">
  <p><b>精通电磁仿真与天线/阵列设计：</b>深度使用 HFSS、CST 进行全波仿真及 RF 模块电磁仿真（博士论文核心工具）；精通特征模式分析（CMA）及其在天线可行性论证、方向图综合、偶极子与阵列模式管理中的应用（首次提出 CMA 基函数加权可行性论证方法，揭示色散效应为宽带阵列设计核心瓶颈）；掌握矩量法、模态分析、近远场变换等电磁理论与计算方法；精通微波暗室天线近远场测试、CNAS 第三方认证测试经验。</p>
  <p><b>精通 AI 辅助天线设计（AI4S）：</b>技能储备包括（1）深度卷积变分自编码器（DCVAE）、VAE 生成模型，实现天线/超构表面结构↔性能双向逆向设计；（2）搭建数百台服务器并行仿真基础设施（行业首创，300× 加速）；（3）PSO/遗传/代理模型优化算法结合 CMA 物理先验驱动 AI 联合优化。</p>
  <p><b>硬件与工程能力：</b>具备从仿真到实物的完整工程闭环能力：PCB 设计与焊接、STM32 嵌入式开发、毫米波雷达调试、铝合金/黄铜样机制备（含 3D 打印治具）；物理样机均经微波暗室实测验证，两项成果通过 CNAS 第三方认证。</p>
  <p><b>开源影响力（可验证工程能力）：</b>GitHub 浏览量 <b>10 万+</b>，天线/超构表面领域排名第一；开发 ARIA 天线 AI 设计智能体；Bilibili 演示视频破万播放，验证方法可复现、可落地。编程：Python（主力）、MATLAB、C。</p>
  <p><b>优秀的数理基础与语言能力：</b>优秀的中英文沟通与写作能力；国际会议报告及获奖经验（PIERS 2024 受邀报告）。</p>
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
<div class="sec-title">发表论文（共 8 篇，含 1 篇在写；按 A 方向相关性排序）</div>
<ol class="paper-list">
  <li>
    <b>Xi Chong You</b>, C.T. Gao, F.H. Lin, "Wideband Multi-Mode Tracking Using Near-Field Global-Correlation Method," <i>Electromagnetic Science</i>, vol. 4, no. 1, 0130512, Mar. 2026.
    <span class="paper-note">（IEEE 期刊，Gold Open Access，第一作者）</span>
  </li>
  <li>
    <b>Xi Chong You</b>, F.H. Lin, "Wideband Massive Characteristic-Mode Tracking of Metasurfaces Using Single-Layer Near-Field Global-Correlation (NFGC) Method," <i>2026 IEEE International Workshop on Antenna Technology (iWAT)</i>, DOI: 10.1109/IWAT66946.2026.11501863.
    <span class="paper-note">（IEEE 国际天线技术研讨会，2026，已发表，第一作者，唯一学生作者）</span>
  </li>
  <li>
    <b>Xi Chong You</b>, F.H. Lin, "Tri-mode Fenced-Discone Antenna (FDA) for Ceiling-Mounted MIMO AP," target: <i>IEEE Trans. Antennas Propag.</i>, manuscript in preparation.
    <span class="paper-note">（IEEE TAP，目标投稿，第一作者，唯一学生作者）</span>
  </li>
  <li>
    <b>Xi Chong You</b>, F.H. Lin, "Machine-learning Aided Design (MLAD) of Metasurfaces and Antennas," <i>PIERS 2024</i>, Chengdu.
    <span class="paper-note">（受邀报告 Invited Talk，已发表，第一作者，唯一学生作者）</span>
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
    <b>Xi Chong You</b>, C.T. Gao, F.H. Lin, "Significant Bandwidth Enhancement of Low-Reflection Checkerboard Metasurfaces Using Machine Learning," <i>ISAPE 2024</i>, Hefei.
    <span class="paper-note">（已发表，第一作者）</span>
  </li>
</ol>

</div><!-- end .page -->
</body>
</html>'''

output = head_part + new_body

with open('d:/YXC/YXC_know/Resume/简历/尤栖冲_华为硬件工程院_A方向.html', 'w', encoding='utf-8') as f:
    f.write(output)

print(f"Done! {len(output)} bytes written.")
