import React, { useState, useEffect } from 'react';
import { User } from './server';

const UserList: React.FC = () => {
  const [users, setUsers] = useState<User[]>([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [filters, setFilters] = useState({
    gender: '',
    ageGroup: '',
  });

  useEffect(() => {
    // ユーザーデータの取得（実際のAPIコールに置き換える）
    const fetchUsers = async () => {
      // サンプルデータ
      const sampleUsers: User[] = [
        { id: '1234567890', name: '山田太郎', gender: '男性', age: 35, address: '東京都新宿区1-1-1' },
        { id: '2345678901', name: '佐藤花子', gender: '女性', age: 28, address: '大阪府大阪市中央区2-2-2' },
        // ... その他のユーザー
      ];
      setUsers(sampleUsers);
    };
    fetchUsers();
  }, []);

  const filteredUsers = users.filter(user => 
    (user.id.includes(searchTerm) || user.name.includes(searchTerm)) &&
    (filters.gender === '' || user.gender === filters.gender) &&
    (filters.ageGroup === '' || getAgeGroup(user.age) === filters.ageGroup)
  );

  return (
    <>
      <h2 className="text-2xl font-bold mb-4">避難者リスト</h2>
      <div className="mb-4">
        <input
          type="text"
          placeholder="ID or 氏名で検索"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="border p-2 rounded"
        />
        {/* フィルターのドロップダウンを追加 */}
        <select
          value={filters.gender}
          onChange={(e) => setFilters({...filters, gender: e.target.value})}
          className="border p-2 rounded ml-2"
        >
          <option value="">性別</option>
          <option value="男性">男性</option>
          <option value="女性">女性</option>
        </select>
        <select
          value={filters.ageGroup}
          onChange={(e) => setFilters({...filters, ageGroup: e.target.value})}
          className="border p-2 rounded ml-2"
        >
          <option value="">年代</option>
          <option value="0-9歳">0-9歳</option>
          <option value="10-19歳">10-19歳</option>
          <option value="20-29歳">20-29歳</option>
          <option value="30-39歳">30-39歳</option>
          <option value="40-49歳">40-49歳</option>
          <option value="50-59歳">50-59歳</option>
          <option value="60-69歳">60-69歳</option>
          <option value="70-79歳">70-79歳</option>
          <option value="80歳以上">80歳以上</option>
        </select>
      </div>
      <table className="w-full">
        <thead>
          <tr>
            <th>氏名</th>
            <th>性別</th>
            <th>年代</th>
            <th>住所</th>
          </tr>
        </thead>
        <tbody>
          {filteredUsers.map(user => (
            <tr key={user.id}>
              <td>{user.name}</td>
              <td className="text-center">{user.gender}</td>
              <td className="text-center">{getAgeGroup(user.age)}</td>
              <td>{user.address}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </>
  );
};

const getAgeGroup = (age: number): string => {
  if (age < 10) return '0-9歳';
  if (age < 20) return '10-19歳';
  if (age < 30) return '20-29歳';
  if (age < 40) return '30-39歳';
  if (age < 50) return '40-49歳';
  if (age < 60) return '50-59歳';
  if (age < 70) return '60-69歳';
  if (age < 80) return '70-79歳';
  return '80歳以上';
};

export default UserList;
