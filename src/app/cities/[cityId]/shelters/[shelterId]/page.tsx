'use client'

import React from 'react'
import { PieChart, Pie, Cell, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts'
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"

// Mock data - replace with actual data in production
const shelterData = {
  capacity: 1000,
  currentOccupancy: 750,
  maleCount: 400,
  femaleCount: 350
}

const suppliesData = [
  { name: '食料品', shortage: 5 },
  { name: '日用品・衛生用品', shortage: 3 },
  { name: '医薬品', shortage: 2 },
  { name: 'その他', shortage: 1 },
]

const statusData = [
  { status: '重症', male: 10, female: 8 },
  { status: '軽傷', male: 30, female: 25 },
  { status: '要介護', male: 50, female: 60 },
  { status: '無事', male: 305, female: 255 },
  { status: '死亡', male: 5, female: 2 },
]

const outData = [
  { name: '山田太郎', age: 45, gender: '男性', elapsedTime: '2:30', plannedTime: '2:00' },
  { name: '佐藤花子', age: 32, gender: '女性', elapsedTime: '1:45', plannedTime: '2:00' },
  { name: '鈴木一郎', age: 58, gender: '男性', elapsedTime: '3:15', plannedTime: '3:00' },
]

export default function Dashboard() {
  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">避難所管理ダッシュボード</h1>
      <div className="grid grid-cols-3 gap-4 h-[calc(100vh-100px)]">
        <div className="col-span-1 space-y-4">
          <OccupancyChart />
          <SuppliesChart />
        </div>
        <div className="col-span-2 space-y-4">
          <StatusChart />
          <OutTable />
        </div>
      </div>
    </div>
  )
}

function OccupancyChart() {
  const data = [
    { name: '男性', value: shelterData.maleCount },
    { name: '女性', value: shelterData.femaleCount },
    { name: '残り', value: shelterData.capacity - shelterData.currentOccupancy },
  ]
  const COLORS = ['#0088FE', '#FF8042', '#CCCCCC']

  return (
    <Card>
      <CardHeader>
        <CardTitle>避難所収容状況</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="h-[300px] w-full">
          <ResponsiveContainer width="100%" height={200}>
            <PieChart>
              <Pie
                data={data}
                cx="50%"
                cy="50%"
                innerRadius={60}
                outerRadius={80}
                fill="#8884d8"
                paddingAngle={5}
                dataKey="value"
              >
                {data.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                ))}
              </Pie>
              <Tooltip formatter={(value) => `${value}人`} />
              <text x="50%" y="50%" textAnchor="middle" dominantBaseline="middle">
                {`${shelterData.currentOccupancy}/${shelterData.capacity}`}
              </text>
            </PieChart>
          </ResponsiveContainer>
        </div>
        <div className="mt-4 flex justify-center">
          {data.map((entry, index) => (
            <div key={`legend-${index}`} className="flex items-center mr-4">
              <div className="w-3 h-3 mr-1" style={{ backgroundColor: COLORS[index] }}></div>
              <span>{entry.name}</span>
            </div>
          ))}
        </div>
      </CardContent>
    </Card>
  )
}

function SuppliesChart() {
  return (
    <Card>
      <CardHeader>
        <CardTitle>物資不足状況</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="h-[300px] w-full">
          <ResponsiveContainer width="100%" height={200}>
            <BarChart data={suppliesData} layout="vertical">
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis type="number" />
              <YAxis dataKey="name" type="category" />
              <Tooltip />
              <Bar dataKey="shortage" fill="#8884d8" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </CardContent>
    </Card>
  )
}

function StatusChart() {
  return (
    <Card>
      <CardHeader>
        <CardTitle>避難者ステータス</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="h-[300px] w-full">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={statusData} layout="vertical">
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis type="number" />
              <YAxis dataKey="status" type="category" />
              <Tooltip />
              <Legend />
              <Bar dataKey="male" stackId="a" fill="#0088FE" name="男性" />
              <Bar dataKey="female" stackId="a" fill="#FF8042" name="女性" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </CardContent>
    </Card>
  )
}

function OutTable() {
  return (
    <Card>
      <CardHeader>
        <CardTitle>外出中の避難市民</CardTitle>
      </CardHeader>
      <CardContent>
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>氏名</TableHead>
              <TableHead>年齢</TableHead>
              <TableHead>性別</TableHead>
              <TableHead>経過時間</TableHead>
              <TableHead>予定時間</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {outData.map((person, index) => (
              <TableRow key={index}>
                <TableCell>{person.name}</TableCell>
                <TableCell>{person.age}</TableCell>
                <TableCell>{person.gender}</TableCell>
                <TableCell className={person.elapsedTime > person.plannedTime ? 'text-red-500' : ''}>
                  {person.elapsedTime}
                </TableCell>
                <TableCell>{person.plannedTime}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </CardContent>
    </Card>
  )
}