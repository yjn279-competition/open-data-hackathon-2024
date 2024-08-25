import React, { useState, useEffect } from 'react';

// Evacuee型のインターフェース
interface Evacuee {
  evacuee_id: string;
  is_safety: boolean;
  shelter_code: string;
  allergy_code: string;
  update_at: string;
  create_at: string;
}

const UserList: React.FC = () => {
  const [evacuees, setEvacuees] = useState<Evacuee[]>([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [filters, setFilters] = useState({
    shelter_code: '',
    is_safety: '',
  });

  useEffect(() => {
    // FastAPIのエンドポイントからデータを取得
    const fetchEvacuees = async () => {
      try {
        console.log("Fetching evacuees...");
        const response = await fetch('http://localhost:8000/evacuees/');
        console.log("Response status:", response.status);
        if (!response.ok) {
          console.log("Network response was not ok");
          throw new Error('Network response was not ok');
        }
        const data: Evacuee[] = await response.json();
        console.log("Data fetched:", data);  // 取得したデータをコンソールに表示
        setEvacuees(data);
      } catch (error) {
        console.error('Fetch error:', error);
      }
    };
    fetchEvacuees();
  }, []);

  const filteredEvacuees = evacuees.filter(evacuee =>
    (evacuee.evacuee_id.includes(searchTerm)) &&
    (filters.shelter_code === '' || evacuee.shelter_code === filters.shelter_code) &&
    (filters.is_safety === '' || String(evacuee.is_safety) === filters.is_safety)
  );

  return (
    <div className="container mx-auto">
      <h2 className="text-2xl font-bold mb-4">避難者リスト</h2>
      <div className="mb-4">
        <input
          type="text"
          placeholder="IDで検索"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="border p-2 rounded"
        />
        <select
          value={filters.shelter_code}
          onChange={(e) => setFilters({ ...filters, shelter_code: e.target.value })}
          className="border p-2 rounded ml-2"
        >
          <option value="">避難所コード</option>
          <option value="shel001">shel001</option>
          <option value="shel002">shel002</option>
          <option value="shel003">shel003</option>
        </select>
        <select
          value={filters.is_safety}
          onChange={(e) => setFilters({ ...filters, is_safety: e.target.value })}
          className="border p-2 rounded ml-2"
        >
          <option value="">安否確認</option>
          <option value="true">安全</option>
          <option value="false">危険</option>
        </select>
      </div>
      <table className="w-full border-collapse">
        <thead>
          <tr className="bg-gray-200">
            <th className="border p-2 text-black">避難者ID</th>
            <th className="border p-2 text-black">避難所コード</th>
            <th className="border p-2 text-black">安否確認</th>
            <th className="border p-2 text-black">アレルギーコード</th>
            <th className="border p-2 text-black">更新日時</th>
            <th className="border p-2 text-black">作成日時</th>
          </tr>
        </thead>
        <tbody>
          {filteredEvacuees.map(evacuee => (
            <tr key={evacuee.evacuee_id} className="hover:bg-gray-100">
              <td className="border p-2 text-black">{evacuee.evacuee_id}</td>
              <td className="border p-2 text-black">{evacuee.shelter_code}</td>
              <td className="border p-2 text-center text-black">{evacuee.is_safety ? "安全" : "危険"}</td>
              <td className="border p-2 text-center text-black">{evacuee.allergy_code}</td>
              <td className="border p-2 text-black">{new Date(evacuee.update_at).toLocaleString()}</td>
              <td className="border p-2 text-black">{new Date(evacuee.create_at).toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default UserList;
