'use strict';
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, BorderStyle, WidthType, ShadingType, VerticalAlign,
} = require('docx');
const fs = require('fs');

// ── A4 layout (left 30mm, right 20mm, top/bottom 20mm) ───────────────────────
const PW = 11906, PH = 16838;
const ML = 1701, MR = 1134, MT = 1134, MB = 1134;
const CW = PW - ML - MR; // 9071 DXA

// ── Fonts ─────────────────────────────────────────────────────────────────────
const CH = '宋体';
const HF = '黑体';    // headings
const EN = 'Times New Roman';

// ── Sizes (half-points) ───────────────────────────────────────────────────────
const SZ = {
  title: 44,   // 22pt  二号
  h1: 32,      // 16pt  三号
  h2: 28,      // 14pt  四号
  h3: 26,      // 13pt  小三
  body: 24,    // 12pt  小四
  small: 20,   // 10pt
};

// ── Spacing ───────────────────────────────────────────────────────────────────
const LS15 = { line: 360, lineRule: 'auto' };  // 1.5× line spacing

// ── Borders ───────────────────────────────────────────────────────────────────
const BD  = (color = 'CCCCCC', sz = 6) => ({ style: BorderStyle.SINGLE, size: sz, color });
const CELLBORDER = { top: BD(), bottom: BD(), left: BD(), right: BD() };
const NOBORDER   = { top: BD('FFFFFF', 0), bottom: BD('FFFFFF', 0),
                     left: BD('FFFFFF', 0), right: BD('FFFFFF', 0) };

// ── Run helpers ───────────────────────────────────────────────────────────────
const cr = (text, opts = {}) =>
  new TextRun({ text, font: { name: CH }, size: SZ.body, ...opts });

const er = (text, opts = {}) =>
  new TextRun({ text, font: { name: EN }, size: SZ.body, ...opts });

const hr = (text, opts = {}) =>
  new TextRun({ text, font: { name: HF }, size: SZ.body, bold: true, ...opts });

// ── Paragraph helpers ─────────────────────────────────────────────────────────
// Body paragraph with 2-char first-line indent
function p(children, extraOpts = {}) {
  if (typeof children === 'string') children = [cr(children)];
  return new Paragraph({
    children,
    alignment: AlignmentType.JUSTIFIED,
    spacing: { ...LS15, before: 0, after: 80 },
    indent: { firstLine: 480 },
    ...extraOpts,
  });
}

// Empty line
const blank = () => new Paragraph({
  children: [cr(' ')],
  spacing: { line: 240, lineRule: 'auto', before: 0, after: 0 },
});

// Heading level-1: 一、二、三...
function h1(text) {
  return new Paragraph({
    children: [new TextRun({ text, font: { name: HF }, size: SZ.h1, bold: true })],
    alignment: AlignmentType.LEFT,
    spacing: { ...LS15, before: 320, after: 120 },
  });
}

// Heading level-2: 1.1 / 2.2 ...
function h2(text) {
  return new Paragraph({
    children: [new TextRun({ text, font: { name: HF }, size: SZ.h2, bold: true })],
    alignment: AlignmentType.LEFT,
    spacing: { ...LS15, before: 200, after: 80 },
  });
}

// Mixed-font builder: array of [text, isEnglish?, opts?]
function mx(parts) {
  return parts.map(([text, isEn, opts]) => {
    const base = isEn
      ? { font: { name: EN }, size: SZ.body }
      : { font: { name: CH }, size: SZ.body };
    return new TextRun({ text, ...base, ...(opts || {}) });
  });
}

// Centered paragraph (for title area)
function ctr(children, size = SZ.body, spacing = {}) {
  if (typeof children === 'string')
    children = [new TextRun({ text: children, font: { name: CH }, size, bold: size >= SZ.h1 })];
  return new Paragraph({
    children,
    alignment: AlignmentType.CENTER,
    spacing: { ...LS15, before: 0, after: 80, ...spacing },
  });
}

// Table cell
function tc(children, width, opts = {}) {
  if (typeof children === 'string') {
    children = [new Paragraph({
      children: [cr(children)],
      alignment: AlignmentType.CENTER,
      spacing: { line: 300, lineRule: 'auto', before: 40, after: 40 },
    })];
  }
  return new TableCell({
    children,
    width: { size: width, type: WidthType.DXA },
    borders: CELLBORDER,
    margins: { top: 60, bottom: 60, left: 100, right: 100 },
    verticalAlign: VerticalAlign.CENTER,
    ...opts,
  });
}

function headerCell(text, width) {
  return new TableCell({
    children: [new Paragraph({
      children: [cr(text, { bold: true })],
      alignment: AlignmentType.CENTER,
      spacing: { line: 300, lineRule: 'auto', before: 40, after: 40 },
    })],
    width: { size: width, type: WidthType.DXA },
    borders: CELLBORDER,
    margins: { top: 60, bottom: 60, left: 100, right: 100 },
    shading: { fill: 'D9E1F2', type: ShadingType.CLEAR },
    verticalAlign: VerticalAlign.CENTER,
  });
}

// ── Document ──────────────────────────────────────────────────────────────────
const children = [];

// ── 封面 ──────────────────────────────────────────────────────────────────────
children.push(blank(), blank());

children.push(new Paragraph({
  children: [new TextRun({
    text: 'ARIA：AI 驱动天线设计智能体',
    font: { name: HF }, size: SZ.title, bold: true,
  })],
  alignment: AlignmentType.CENTER,
  spacing: { ...LS15, before: 0, after: 200 },
}));

children.push(new Paragraph({
  children: [new TextRun({
    text: 'Antenna Resonance Intelligence Architect',
    font: { name: EN }, size: SZ.h2, bold: false,
  })],
  alignment: AlignmentType.CENTER,
  spacing: { ...LS15, before: 0, after: 80 },
}));

children.push(blank());

children.push(ctr(mx([
  ['参赛队伍：尤栖冲（上海科技大学 信息科学与技术学院）', false]
])));
children.push(ctr(mx([
  ['开源主页：', false],
  ['github.com/youxch', true],
])));
children.push(ctr(mx([
  ['演示视频：', false],
  ['bilibili.com/video/BV1dEw5zWE4k', true],
])));

children.push(blank(), blank());

// ── 一、引言与应用背景 ─────────────────────────────────────────────────────────
children.push(h1('一、引言与应用背景'));

children.push(p(mx([
  ['天线是现代无线通信、雷达探测、卫星互联网等系统的核心辐射部件，其设计质量直接决定系统整体性能。然而传统天线设计高度依赖工程师经验与耗时的数值迭代：以超表面天线为例，一次全波仿真约需5分钟，若对全部候选结构逐一仿真，单个设计任务的计算周期往往以月计。即便借助参数扫描或粒子群优化等传统算法，设计流程也难以脱离"设置-仿真-评估-调整"的反复循环，效率瓶颈突出，难以满足工业界快速迭代的需求。', false],
])));

children.push(p(mx([
  ['近年来，深度学习与生成式机器学习方法被引入天线设计领域，已在特定结构类型上展现出显著的效率优势。然而，现有研究大多停留于单一结构类型的验证阶段，尚缺乏将自然语言交互、电磁建模、智能优化与结果展示整合为统一工作流的系统级工程实现。', false],
  ['ARIA', true],
  ['（Antenna Resonance Intelligence Architect）', false],
  ['正是针对上述痛点提出的', false],
  ['AI', true],
  ['驱动天线设计智能体系统。系统以自然语言作为输入接口，通过五层架构自动完成从需求解析、参数化电磁建模、代理模型加速优化到结果输出的全流程闭环。目前，', false],
  ['ARIA', true],
  ['已支持矩形贴片、半波偶极子、像素化贴片及反射超表面等多类结构，集成贝叶斯优化、粒子群算法（', false],
  ['PSO', true],
  ['）、差分进化（', false],
  ['DE', true],
  ['）及生成式深度网络四种求解策略，并已通过五项独立实验完成工程验证。', false],
])));

// ── 二、系统总体架构 ──────────────────────────────────────────────────────────
children.push(h1('二、系统总体架构'));

children.push(p(mx([
  ['ARIA', true],
  ['系统由五个功能层次顺序衔接构成，各层职能清晰，接口标准统一。', false],
])));

children.push(p(mx([
  ['第一层为', false],
  ['自然语言输入层', false, { bold: true }],
  ['，负责接收用户以文字描述的天线设计需求，如"设计工作于', false],
  ['2.4 GHz', true],
  ['、增益不低于', false],
  ['6 dBi', true],
  ['的低剖面贴片天线"。该层将非结构化语言转化为结构类型标识与目标指标向量，支持关键词解析与上下文模糊匹配两种模式。', false],
])));

children.push(p(mx([
  ['第二层为', false],
  ['CST 建模层', false, { bold: true }],
  ['，根据解析结果自动调用', false],
  ['CST Microwave Studio', true],
  ['的', false],
  ['Python API', true],
  ['，完成几何结构的参数化建模与电磁仿真配置。系统内置矩形贴片、半波偶极子、像素化贴片（', false],
  ['25—100', true],
  ['维设计自由度）及反射超表面四类结构的参数化模板，覆盖从标准设计到高维拓扑优化的不同复杂度场景。', false],
])));

children.push(p(mx([
  ['第三层为', false],
  ['代理模型层', false, { bold: true }],
  ['，是系统实现高效优化的关键。该层部署预训练的深度学习代理网络，以毫秒级时延替代耗时的全波仿真，为优化算法提供低成本的电磁性能评估函数，综合加速比超过60倍。', false],
])));

children.push(p(mx([
  ['第四层为', false],
  ['优化算法层', false, { bold: true }],
  ['，根据设计变量维度与目标函数形态动态配置求解策略。对于连续参数优化问题，系统优先采用贝叶斯优化或', false],
  ['PSO', true],
  ['；对于高维离散拓扑问题，则调用生成式深度神经网络直接生成满足指标的候选结构，避免逐一枚举带来的组合爆炸。', false],
])));

children.push(p(mx([
  ['第五层为', false],
  ['结果展示层', false, { bold: true }],
  ['，将', false],
  ['S11', true],
  ['曲线、方向图、增益带宽数据及三维结构图自动归档，生成标准化设计报告，并提供与全波仿真结果的误差对比核验。', false],
])));

children.push(p(mx([
  ['从工作流角度，一次完整的', false],
  ['ARIA', true],
  ['设计任务遵循如下流程：自然语言需求输入 → 解析为结构类型与指标约束 → 自动初始化参数 →', false],
  ['CST', true],
  ['参数化建模与时域仿真 → 代理模型接管优化迭代 → 输出满足指标的参数及性能报告。每一环节均具有良好的扩展性，为后续新增结构类型与优化算法奠定了工程基础。值得指出的是，', false],
  ['ARIA', true],
  ['并非将', false],
  ['AI', true],
  ['作为孤立模块嵌入传统流程，而是以智能驱动替代了传统设计中复杂度最高、重复性最强的"迭代仿真＋人工判断"环节，使工程师能够将精力集中于指标定义与方案决策。', false],
])));

// ── 三、核心技术方法 ──────────────────────────────────────────────────────────
children.push(h1('三、核心技术方法'));

children.push(h2('3.1  统计分布随机筛选法（SRDF）'));

children.push(p(mx([
  ['天线', false],
  ['AI', true],
  ['设计的核心挑战之一在于以最低仿真成本构建高质量训练数据集。传统"大数据"方法需对数万个候选单元格逐一开展全波仿真：若每次仿真耗时5分钟，10,000个样本的数据采集周期超过一个月，成本极为高昂。', false],
])));

children.push(p(mx([
  ['ARIA', true],
  ['采用无需任何物理先验知识的统计分布随机筛选法（', false],
  ['Statistically Random Data Filtering, SRDF', true],
  ['）解决上述问题。其核心思路是：在仿真之前，依据单元格几何编码的统计特征——即12×12网格中导体像素单元（', false],
  ['pico-cell', true],
  ['）的填充率分布——从约3300万候选结构中按统计比例随机抽取代表性样本，确保训练集在几何空间上具有均匀覆盖性，而非向特定性能区间偏斜。', false],
])));

children.push(p(mx([
  ['以反射超表面设计为例，', false],
  ['SRDF', true],
  ['从3300万候选结构中筛选出2400个样本（占总量的0.01%），对应约半周时间的仿真工作量。基于此2400个样本，训练深度卷积变分自编码器（', false],
  ['DCVAE', true],
  ['）网络，建立单元格几何编码与8–12 GHz反射相位之间的双向映射。训练完成的网络可在数秒内完成正向性能预测与逆向结构生成，预测精度满足工程设计要求。', false],
])));

children.push(p(mx([
  ['SRDF', true],
  ['方法的核心优势体现在三个方面：', false],
  ['（1）数据规模降至候选空间的0.01%，仿真成本降低约99%；', false],
  ['（2）无需针对特定频段、材料或结构类型引入先验知识，具有普遍适用性，可直接迁移至不同设计任务；', false],
  ['（3）通过统计均匀覆盖反射相位空间，训练数据的分布均衡性优于经验驱动的采样方法，有利于提升网络在稀疏区域的泛化能力。', false],
])));

children.push(h2('3.2  生成式机器学习拓扑设计'));

children.push(p(mx([
  ['对于高维拓扑优化问题（如像素化超表面设计），传统方法通过参数扫描或迭代优化搜索满足指标的结构，计算复杂度随设计自由度指数增长。', false],
  ['ARIA', true],
  ['引入生成式机器学习方法，将"搜索"转化为"生成"，从根本上改变了设计效率的上限。', false],
])));

children.push(p(mx([
  ['DCVAE', true],
  ['网络将单元格几何编码矩阵', false],
  ['C（12×12）', true],
  ['与反射相位向量', false],
  ['Φ（40×1）', true],
  ['同时映射到二维隐空间，使两个异质信息空间在统一的低维表示中建立关联。利用训练后的网络，可通过对隐空间中2400个已知锚点的插值，在20分钟内生成200万个新结构的几何与性能预测，全程无需额外仿真，预测相位与仿真结果的相似度高于94%。在此200万候选结构中，通过', false],
  ['CityHash', true],
  ['快速搜索算法，可在5秒内完成对任意指定方向（误差≤5°）的最优单元格组合筛选，设计效率较传统迭代优化提升约', false],
  ['3', true],
  ['个数量级。', false],
])));

children.push(p(mx([
  ['生成式方法的核心意义在于突破性能上界。传统优化在预定义候选集内搜索最优解，性能上界受限于先验知识所划定的设计空间；而生成式网络通过隐空间插值创造出训练集之外的新结构，使系统得以探索并突破已知设计的性能边界——这一能力在后文实验五中得到了直接量化验证。', false],
])));

children.push(h2('3.3  代理模型驱动的多结构统一优化框架'));

children.push(p(mx([
  ['在', false],
  ['ARIA', true],
  ['的优化架构中，代理模型承担替代全波仿真、为优化算法提供高效评估函数的核心角色。全波仿真每次耗时约5分钟，而代理模型的预测时延仅为毫秒量级，使得原本需要数天的优化迭代过程压缩至分钟级，综合加速比超过60倍。', false],
])));

children.push(p(mx([
  ['ARIA', true],
  ['对不同结构类型部署了差异化的代理模型与优化策略组合。对于连续参数优化问题，多层感知机（', false],
  ['MLP', true],
  ['）网络在3456个仿真样本的基础上建立结构参数与', false],
  ['S11', true],
  ['、增益之间的映射，配合贝叶斯优化或', false],
  ['PSO', true],
  ['，可在扩展参数空间内预测超过400万种候选结构的性能，并筛选出满足多目标约束的最优设计。对于高维像素拓扑问题，则采用第3.2节所述的生成式', false],
  ['DCVAE', true],
  ['框架，以插值代替搜索，实现大规模候选结构的秒级生成。', false],
])));

children.push(p(mx([
  ['统一框架的工程价值在于：无论矩形贴片、像素化超表面还是棋盘超表面等不同结构类型，均通过相同的"结构编码 → 代理评估 → 优化筛选"三步流程处理，系统根据输入结构类型自动匹配最优求解路径，用户无需关注底层算法细节。这一设计不仅降低了使用门槛，也为系统后续扩展新结构类型提供了可复用的工程基础。', false],
])));

// ── 四、系统实验验证 ──────────────────────────────────────────────────────────
children.push(h1('四、系统实验验证'));

children.push(p(mx([
  ['本节通过五项独立实验对', false],
  ['ARIA', true],
  ['系统进行全面验证，涵盖反射超表面、低剖面贴片、多波束超表面、性能边界逼近及低反射棋盘超表面等不同结构类型与设计目标。', false],
])));

children.push(h2('实验一：反射超表面逆向设计'));

children.push(p(mx([
  ['本实验验证', false],
  ['SRDF', true],
  ['方法与', false],
  ['DCVAE', true],
  ['网络在反射超表面单元格逆向设计中的有效性。以工作于10 GHz的反射超表面天线为目标，', false],
  ['ARIA', true],
  ['基于2400个', false],
  ['SRDF', true],
  ['筛选样本完成网络训练，并自动设计波束分别指向偏主波束方向30°与60°的两种超表面天线方案。', false],
])));

children.push(p(mx([
  ['实验结果表明：单元格相位覆盖范围达到360°，各单元格相位偏差小于15°，实测波束指向偏差小于3°，仿真结果与暗室测量结果高度吻合。该实验充分验证了', false],
  ['AI', true],
  ['方法在高维散射体结构设计中的有效性，同时证明仅需0.01%的候选样本即可支撑工程精度要求的网络训练。', false],
])));

children.push(h2('实验二：低剖面宽带微带贴片天线设计'));

children.push(p(mx([
  ['本实验针对低剖面微带贴片天线的多频段覆盖需求，通过', false],
  ['MLP', true],
  ['代理模型建立结构参数与', false],
  ['S11', true],
  ['、增益之间的映射关系，在扩展参数空间内筛选满足指标的候选结构。', false],
])));

children.push(p(mx([
  ['ARIA', true],
  ['自动设计出覆盖2.4 GHz、2.6 GHz与3.3 GHz三个频段的贴片天线：2.4 GHz频段增益6.5 dBi（带宽8%），2.6 GHz频段增益6.2 dBi（带宽7%），3.3 GHz频段增益5.8 dBi（带宽6%）。代理模型预测值与', false],
  ['CST', true],
  ['全波仿真结果的误差均小于5%，可直接作为工程中可行结构的快速参考设计，验证了连续参数优化框架的精度与适用性。', false],
])));

children.push(h2('实验三：多波束超表面生成式设计'));

children.push(p(mx([
  ['本实验展示生成式', false],
  ['MLAD', true],
  ['方法在多波束超表面天线设计中的能力。', false],
  ['ARIA', true],
  ['基于2400个训练样本在隐空间内插值生成200万个新结构，从中筛选出单波束（', false],
  ['θ', true],
  ['max=60°）和双波束（', false],
  ['θ', true],
  ['max=−15°及30°）两种超表面方案，整个生成与筛选过程耗时仅约20分钟。', false],
])));

children.push(p(mx([
  ['实验制造了单波束（', false],
  ['θ', true],
  ['max=60°）原型并完成暗室测量：实测与仿真方向图在正向半球内吻合良好，双波束方案两个峰值方向与预测值误差均小于2°，实测交叉极化电平低于', false],
  ['−34 dB', true],
  ['。较之传统迭代优化所需2–3天的设计周期，', false],
  ['ARIA', true],
  ['将设计时间压缩至秒级，展现了生成式设计路径的工程可靠性与高效性。', false],
])));

children.push(h2('实验四：微带天线性能边界逼近'));

children.push(p(mx([
  ['本实验验证', false],
  ['MLAD', true],
  ['方法在逼近微带天线增益带宽积性能上界方面的能力。基于', false],
  ['MLP', true],
  ['网络对3456个训练样本建立的映射模型，', false],
  ['ARIA', true],
  ['在扩展设计空间内快速预测400万种候选结构，从中筛选出在2.4 GHz与3.3 GHz双频段均具备较高增益带宽积的U槽贴片天线方案。', false],
])));

children.push(p(mx([
  ['设计天线在2.45 GHz实测增益8.8 dBi，在3.3 GHz实测增益7.4 dBi，增益带宽积超过训练集中所有已知设计，', false],
  ['E', true],
  ['面/H面方向图对称性良好，旁瓣电平低于', false],
  ['−20 dB', true],
  ['。实验表明，在多维性能空间的探索中，生成式框架相较于传统单目标优化方法具有明显优越性，能够在无需预先知晓性能上界的条件下自动发现更优设计。', false],
])));

children.push(h2('实验五：低反射棋盘超表面带宽增强'));

children.push(p(mx([
  ['本实验针对低反射棋盘超表面的雷达散射截面（', false],
  ['RCS', true],
  ['）缩减性能优化问题。', false],
  ['ARIA', true],
  ['通过条件深度神经网络（', false],
  ['cDNN', true],
  ['）在12×12像素编码空间内大规模生成新型反相单元格，并自动选择使棋盘超表面10 dB散射缩减带宽最大化的单元格组合。', false],
])));

children.push(p(mx([
  ['最终设计在3.89–10.72 GHz范围内实现10 dB RCS缩减，带宽达84%，相较训练集中最优样本（带宽62%）提升22个百分点。下表给出本工作与代表性文献的定量对比：', false],
])));

// Comparison table
const colW = [CW * 0.12, CW * 0.44, CW * 0.22, CW * 0.22].map(Math.round);
children.push(new Table({
  width: { size: CW, type: WidthType.DXA },
  columnWidths: colW,
  rows: [
    new TableRow({
      children: [
        headerCell('参考', colW[0]),
        headerCell('主要特点', colW[1]),
        headerCell('相位差带宽', colW[2]),
        headerCell('10 dB缩减带宽', colW[3]),
      ],
    }),
    new TableRow({ children: [
      tc('[1]', colW[0]), tc('棋盘EBG超表面，经典方案', colW[1]),
      tc('66%', colW[2]), tc('62%', colW[3]),
    ]}),
    new TableRow({ children: [
      tc('[2]', colW[0]), tc('双极化棋盘超表面', colW[1]),
      tc('63%', colW[2]), tc('61%', colW[3]),
    ]}),
    new TableRow({ children: [
      tc('[3]', colW[0]), tc('AMC宽带设计', colW[1]),
      tc('75%', colW[2]), tc('74%', colW[3]),
    ]}),
    new TableRow({ children: [
      tc('本工作', colW[0], { shading: { fill: 'E2EFDA', type: ShadingType.CLEAR } }),
      tc('ARIA生成式cDNN设计（像素单元）', colW[1], { shading: { fill: 'E2EFDA', type: ShadingType.CLEAR } }),
      tc('86%（最高）', colW[2], { shading: { fill: 'E2EFDA', type: ShadingType.CLEAR } }),
      tc('84%（最高）', colW[3], { shading: { fill: 'E2EFDA', type: ShadingType.CLEAR } }),
    ]}),
  ],
}));

children.push(new Paragraph({
  children: [cr('表4-1  棋盘超表面10 dB散射缩减带宽对比', { size: SZ.small })],
  alignment: AlignmentType.CENTER,
  spacing: { line: 300, lineRule: 'auto', before: 60, after: 120 },
}));

children.push(p(mx([
  ['在180°±37°相位差带宽与10 dB散射缩减带宽两项指标上，本工作均为现有文献中的最高值，是', false],
  ['ARIA', true],
  ['通过生成式设计突破传统工程优化性能边界的有力例证。', false],
])));

children.push(p(mx([
  ['综合五项实验，', false],
  ['ARIA', true],
  ['系统在多结构类型（超表面、贴片、棋盘结构）、多设计目标（波束指向、增益、带宽、RCS缩减）及多优化范式（逆向预测、生成式设计、性能边界突破）三个维度上均展现出系统性能力。与传统数值仿真迭代相比，', false],
  ['ARIA', true],
  ['可将完整设计周期从数天压缩至分钟级，在效率提升的同时通过实验测量验证了设计的工程可靠性。', false],
])));

// ── 五、结论 ──────────────────────────────────────────────────────────────────
children.push(h1('五、结论'));

children.push(p(mx([
  ['ARIA', true],
  ['是一套以人工智能为核心驱动力的天线设计自动化系统，通过五层架构将自然语言设计需求转化为经仿真验证的天线方案。系统的核心技术创新体现在三个层面：其一，统计分布随机筛选法（', false],
  ['SRDF', true],
  ['）将仿真样本需求压缩至候选空间的0.01%，在无需物理先验的前提下实现高效训练数据采集，该方法具有结构类型无关性，可直接迁移至不同设计任务；其二，生成式机器学习方法通过隐空间插值在数分钟内生成数百万候选设计，突破了传统优化方法受限于预定义候选集的性能上界，在棋盘超表面实验中实现了超越训练集最优22个百分点的带宽增益；其三，代理模型驱动的统一优化框架支持多结构类型的统一调度，实现超过60倍的综合加速。', false],
])));

children.push(p(mx([
  ['五组实验涵盖从反射超表面到棋盘超表面、从单频贴片到多频双波束天线等多种工程场景，实测与仿真的高度吻合验证了', false],
  ['ARIA', true],
  ['在工程实践中的可靠性。系统已开源发布（', false],
  ['GitHub: github.com/youxch', true],
  ['），核心算法对应论文已发表于', false],
  ['Microw. Opt. Technol. Lett.', true],
  ['及', false],
  ['IEEE', true],
  ['系列国际会议，具备直接工业化应用的基础条件。', false],
])));

// ── Build & save ──────────────────────────────────────────────────────────────
const doc = new Document({
  sections: [{
    properties: {
      page: {
        size: { width: PW, height: PH },
        margin: { top: MT, right: MR, bottom: MB, left: ML },
      },
    },
    children,
  }],
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync('ARIA参赛报告_v2.docx', buf);
  console.log('✓  ARIA参赛报告_v2.docx  written');
}).catch(err => { console.error(err); process.exit(1); });
