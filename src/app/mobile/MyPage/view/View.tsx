import { useState } from 'react';
import Link from 'next/link';

const View = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  // ダミーのユーザー情報
  const userInfo = {
    myNumber: '1234567890123',
    name: '山田 太郎',
    gender: '男性',
    age: 35,
    address: '東京都新宿区西新宿2-8-1',
    phoneNumber: '03-1234-5678'
  };

  return (
    <>
    <div className="flex flex-col h-screen">
      {/* Header */}
      <header className="fixed top-0 left-0 right-0 bg-blue-500 text-white p-4 flex items-center z-10">
        <button
          onClick={() => setIsMenuOpen(!isMenuOpen)}
          className="text-2xl mr-4"
        >
          ☰
        </button>
        <h1 className="text-xl font-bold">ユーザー情報</h1>
      </header>

      {/* Side Menu */}
      {isMenuOpen && (
        <div className="fixed inset-0 bg-gray-800 bg-opacity-75 z-50">
          <div className="bg-white h-full w-64 shadow-lg">
            <div className="p-4">
              <button
                onClick={() => setIsMenuOpen(false)}
                className="text-2xl mb-4"
              >
                ×
              </button>
              <nav>
                <ul>
                  <li><Link href="/" className="block py-2">TOPページ</Link></li>
                  <li><Link href="/info" className="block py-2">情報一覧</Link></li>
                  {/* 他のメニュー項目 */}
                </ul>
              </nav>
            </div>
          </div>
        </div>
      )}

      {/* Main Content */}
      <main className="flex-grow mt-16 p-4 overflow-y-auto">
        <div className="bg-white rounded-lg shadow p-4">
          <h2 className="text-2xl font-semibold mb-4">ユーザー情報</h2>
          <table className="w-full">
            <tbody>
              <tr>
                <td className="font-semibold pr-4 py-2">マイナンバー:</td>
                <td>{userInfo.myNumber}</td>
              </tr>
              <tr>
                <td className="font-semibold pr-4 py-2">氏名:</td>
                <td>{userInfo.name}</td>
              </tr>
              <tr>
                <td className="font-semibold pr-4 py-2">性別:</td>
                <td>{userInfo.gender}</td>
              </tr>
              <tr>
                <td className="font-semibold pr-4 py-2">年齢:</td>
                <td>{userInfo.age}歳</td>
              </tr>
              <tr>
                <td className="font-semibold pr-4 py-2">住所:</td>
                <td>{userInfo.address}</td>
              </tr>
              <tr>
                <td className="font-semibold pr-4 py-2">電話番号:</td>
                <td>{userInfo.phoneNumber}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </main>
    </div></>
  );
};

export default View;