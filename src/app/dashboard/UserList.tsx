import React, { useState, useEffect } from 'react';

// Evacuee型のインターフェース
interface Evacuee {
  full_name: string;
  birth_date: string;
  address: string;
  is_safety: boolean;
  shelter_name: string;
  shelter_address: string;
}

const UserList: React.FC = () => {
  const [evacuees, setEvacuees] = useState<Evacuee[]>([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [filters, setFilters] = useState({
    shelter_name: '',
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
    (evacuee.full_name.includes(searchTerm) || evacuee.address.includes(searchTerm)) &&
    (filters.shelter_name === '' || evacuee.shelter_name === filters.shelter_name) &&
    (filters.is_safety === '' || String(evacuee.is_safety) === filters.is_safety)
  );

  return (
    <div className="container mx-auto">
      <h2 className="text-2xl font-bold mb-4">避難者リスト</h2>
      <div className="mb-4">
        <input
          type="text"
          placeholder="氏名または住所で検索"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="border p-2 rounded text-black"
        />
        <select
          value={filters.shelter_name}
          onChange={(e) => setFilters({ ...filters, shelter_name: e.target.value })}
          className="border p-2 rounded ml-2 text-black"
        >
          <option value="">避難所</option>
          <option value="避難所A">避難所A</option>
          <option value="避難所B">避難所B</option>
          <option value="避難所C">避難所C</option>
        </select>
        <select
          value={filters.is_safety}
          onChange={(e) => setFilters({ ...filters, is_safety: e.target.value })}
          className="border p-2 rounded ml-2 text-black"
        >
          <option value="">安否確認</option>
          <option value="true">安全</option>
          <option value="false">危険</option>
        </select>
      </div>
      <table className="w-full border-collapse">
        <thead>
          <tr className="bg-gray-200">
            <th className="border p-2 text-black">氏名</th>
            <th className="border p-2 text-black">生年月日</th>
            <th className="border p-2 text-black">住所</th>
            <th className="border p-2 text-black">安否確認</th>
            <th className="border p-2 text-black">避難所名</th>
            <th className="border p-2 text-black">避難所住所</th>
          </tr>
        </thead>
        <tbody>
          {filteredEvacuees.map(evacuee => (
            <tr key={evacuee.full_name} className="hover:bg-gray-100">
              <td className="border p-2 text-black">{evacuee.full_name}</td>
              <td className="border p-2 text-black">{new Date(evacuee.birth_date).toLocaleDateString()}</td>
              <td className="border p-2 text-black">{evacuee.address}</td>
              <td className="border p-2 text-center text-black">{evacuee.is_safety ? "安全" : "危険"}</td>
              <td className="border p-2 text-black">{evacuee.shelter_name}</td>
              <td className="border p-2 text-black">{evacuee.shelter_address}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default UserList;
