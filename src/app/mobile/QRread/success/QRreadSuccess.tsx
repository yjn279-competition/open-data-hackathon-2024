import { useState } from 'react';
import Link from 'next/link';

const QRreadSuccess = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const shelterInfo = {
    name: '素晴らしい避難所',
    addressNumber: '000-0000',
    address: '東京都新宿区西新宿2-8-1',
    phoneNumber: '03-1234-5678'
  };

  const myNumber = '123456789';

  return (
    <div className="flex flex-col h-screen">
      {/* Header */}
      <header className="fixed top-0 left-0 right-0 bg-blue-500 text-white p-4 flex items-center">
        <button
          onClick={() => setIsMenuOpen(!isMenuOpen)}
          className="text-2xl mr-4"
        >
          ☰
        </button>
        <h1 className="text-xl font-bold">みえるーむ</h1>
      </header>

      {/* Side Menu */}
      {isMenuOpen && (
        <div className="fixed inset-0 bg-gray-800 bg-opacity-75 z-50">
          <div className="bg-white h-full w-64 shadow-lg">
            <div className="p-4">
              <button
                onClick={() => setIsMenuOpen(false)}
                className="text-2xl mb-4 text-black"
              >
                ×
              </button>
              <nav>
                <ul>
                  <li><Link href="/mobile" className="block py-2 text-black">TOPページ</Link></li>
                  <li><Link href="/mobile/MyPage/view" className="block py-2 text-black">ユーザー情報</Link></li>
                  <li><Link href="/mobile/QRread/success" className="block py-2 text-black">QRコード読み取り</Link></li>
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
          <h2 className="text-2xl font-semibold mb-4 text-black">避難先登録完了</h2>
          <table className="w-full">
            <tbody>
              <tr>
                <td className="font-semibold pr-4 py-2 text-black">避難所:</td>
                <td className="text-black">{shelterInfo.name}</td>
              </tr>
              <tr>
                <td className="font-semibold pr-4 py-2 text-black">郵便番号：</td>
                <td className="text-black">{shelterInfo.addressNumber}</td>
              </tr>
              <tr>
                <td className="font-semibold pr-4 py-2 text-black">住所:</td>
                <td className="text-black">{shelterInfo.address}</td>
              </tr>
              <tr>
                <td className="font-semibold pr-4 py-2 text-black">電話番号:</td>
                <td className="text-black">{shelterInfo.phoneNumber}</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div className="bg-white rounded-lg shadow p-4 mt-5">
          <h4 className="text-2xl font-semibold mb-4 text-black">あなたのマイナンバー：</h4>
          <a className='text-black'>{myNumber}</a>
        </div>
        <div className="bg-white rounded-lg shadow p-4 mt-5">
          <button className="text-black"><Link href="/mobile">TOPページに戻る</Link></button>
        </div>
      </main>
    </div>
  );
};

export default QRreadSuccess;