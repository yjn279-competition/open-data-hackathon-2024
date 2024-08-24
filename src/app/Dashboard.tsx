'use client'
import React, { useEffect, useRef } from 'react';
import * as d3 from 'd3';

const EvacueeDashboard = () => {
  const svgRef = useRef();

  useEffect(() => {
    // サンプルデータ (変更なし)
    const data = {
      evacueeCapacity: {
        total: 1000,
        current: 750,
        male: 400,
        female: 350
      },
      ageDistribution: [
        { ageGroup: '0-9', count: 50 },
        { ageGroup: '10-19', count: 100 },
        { ageGroup: '20-29', count: 150 },
        { ageGroup: '30-39', count: 120 },
        { ageGroup: '40-49', count: 100 },
        { ageGroup: '50-59', count: 80 },
        { ageGroup: '60-69', count: 70 },
        { ageGroup: '70-79', count: 50 },
        { ageGroup: '80+', count: 30 }
      ],
      allergenDistribution: [
        { allergen: '卵', count: 50 },
        { allergen: '乳', count: 40 },
        { allergen: '小麦', count: 30 },
        { allergen: 'そば', count: 10 },
        { allergen: '落花生', count: 15 },
        { allergen: 'えび', count: 20 },
        { allergen: 'かに', count: 10 }
      ]
    };

    const svg = d3.select(svgRef.current);
    svg.selectAll("*").remove();

    const width = 900;
    const height = 500;
    svg.attr('width', width).attr('height', height);

    // カラーパレット
    const colors = ['#6C63FF', '#FF6584', '#43A047', '#FFA726', '#26C6DA'];

    // 1. 避難所のキャパシティに対する避難者の割合（円グラフ）
    const pieWidth = width / 3;
    const pieHeight = height;
    const pieRadius = Math.min(pieWidth, pieHeight) / 2 * 0.8;

    const pieData = [
      { label: '避難者', value: data.evacueeCapacity.current },
      { label: '空き', value: data.evacueeCapacity.total - data.evacueeCapacity.current }
    ];

    const pieColor = d3.scaleOrdinal()
      .domain(pieData.map(d => d.label))
      .range([colors[0], colors[1]]);

    const pie = d3.pie().value(d => d.value);
    const arc = d3.arc().innerRadius(pieRadius * 0.6).outerRadius(pieRadius);

    const pieGroup = svg.append('g')
      .attr('transform', `translate(${pieWidth / 2}, ${pieHeight / 2})`);

    pieGroup.selectAll('path')
      .data(pie(pieData))
      .enter()
      .append('path')
      .attr('d', arc)
      .attr('fill', d => pieColor(d.data.label))
      .transition()
      .duration(1000)
      .attrTween('d', function(d) {
        const i = d3.interpolate(d.startAngle, d.endAngle);
        return function(t) {
          d.endAngle = i(t);
          return arc(d);
        }
      });

    pieGroup.append('text')
      .attr('text-anchor', 'middle')
      .attr('dy', '-0.5em')
      .attr('font-size', '16px')
      .attr('font-weight', 'bold')
      .text(`${data.evacueeCapacity.current}/${data.evacueeCapacity.total}`);

    pieGroup.append('text')
      .attr('text-anchor', 'middle')
      .attr('dy', '1.5em')
      .attr('font-size', '12px')
      .text(`男性: ${data.evacueeCapacity.male} 女性: ${data.evacueeCapacity.female}`);

    // 2. 年代ごとの避難者の実人数（棒グラフ）
    const barWidth = width * 2 / 3;
    const barHeight = height / 2;
    const barMargin = { top: 30, right: 20, bottom: 30, left: 40 };

    const barX = d3.scaleBand()
      .range([0, barWidth - barMargin.left - barMargin.right])
      .domain(data.ageDistribution.map(d => d.ageGroup))
      .padding(0.2);

    const barY = d3.scaleLinear()
      .range([barHeight - barMargin.top - barMargin.bottom, 0])
      .domain([0, d3.max(data.ageDistribution, d => d.count)]);

    const ageGroup = svg.append('g')
      .attr('transform', `translate(${pieWidth + barMargin.left}, ${barMargin.top})`);

    ageGroup.selectAll('.bar')
      .data(data.ageDistribution)
      .enter().append('rect')
      .attr('class', 'bar')
      .attr('x', d => barX(d.ageGroup))
      .attr('width', barX.bandwidth())
      .attr('y', barHeight - barMargin.top - barMargin.bottom)
      .attr('height', 0)
      .attr('fill', colors[2])
      .transition()
      .duration(1000)
      .attr('y', d => barY(d.count))
      .attr('height', d => barHeight - barMargin.top - barMargin.bottom - barY(d.count));

    ageGroup.append('g')
      .attr('transform', `translate(0, ${barHeight - barMargin.top - barMargin.bottom})`)
      .call(d3.axisBottom(barX))
      .selectAll('text')
      .style('text-anchor', 'end')
      .attr('dx', '-.8em')
      .attr('dy', '.15em')
      .attr('transform', 'rotate(-45)');

    ageGroup.append('g')
      .call(d3.axisLeft(barY));

    ageGroup.append('text')
      .attr('x', (barWidth - barMargin.left - barMargin.right) / 2)
      .attr('y', -10)
      .attr('text-anchor', 'middle')
      .attr('font-size', '14px')
      .attr('font-weight', 'bold')
      .text('年代ごとの避難者数');

    // 3. 主要アレルゲンごとの避難者の実人数（棒グラフ）
    const allergenGroup = svg.append('g')
      .attr('transform', `translate(${pieWidth + barMargin.left}, ${barHeight + barMargin.top})`);

    const allergenX = d3.scaleBand()
      .range([0, barWidth - barMargin.left - barMargin.right])
      .domain(data.allergenDistribution.map(d => d.allergen))
      .padding(0.2);

    const allergenY = d3.scaleLinear()
      .range([barHeight - barMargin.top - barMargin.bottom, 0])
      .domain([0, d3.max(data.allergenDistribution, d => d.count)]);

    allergenGroup.selectAll('.bar')
      .data(data.allergenDistribution)
      .enter().append('rect')
      .attr('class', 'bar')
      .attr('x', d => allergenX(d.allergen))
      .attr('width', allergenX.bandwidth())
      .attr('y', barHeight - barMargin.top - barMargin.bottom)
      .attr('height', 0)
      .attr('fill', colors[3])
      .transition()
      .duration(1000)
      .attr('y', d => allergenY(d.count))
      .attr('height', d => barHeight - barMargin.top - barMargin.bottom - allergenY(d.count));

    allergenGroup.append('g')
      .attr('transform', `translate(0, ${barHeight - barMargin.top - barMargin.bottom})`)
      .call(d3.axisBottom(allergenX));

    allergenGroup.append('g')
      .call(d3.axisLeft(allergenY));

    allergenGroup.append('text')
      .attr('x', (barWidth - barMargin.left - barMargin.right) / 2)
      .attr('y', -10)
      .attr('text-anchor', 'middle')
      .attr('font-size', '14px')
      .attr('font-weight', 'bold')
      .text('主要アレルゲンごとの避難者数');

  }, []);

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-6 text-center text-gray-800">避難者ダッシュボード</h1>
      <div className="bg-white shadow-lg rounded-lg p-6">
        <svg ref={svgRef}></svg>
      </div>
    </div>
  );
};

export default EvacueeDashboard;
