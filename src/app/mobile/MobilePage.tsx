import { useState } from 'react';
import Link from 'next/link';

const MobilePage = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

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
        {/* User Name */}
        <div className="mb-4">
          <h2 className="text-xl font-semibold">ようこそ、中村 勇士様</h2>
        </div>

        {/* Map */}
        <div className="mb-4 bg-gray-200 h-64 flex items-center justify-center">
          <p>ここにマップが表示されます</p>
        </div>

        {/* Disaster Information */}
        <div className="bg-white rounded-lg shadow p-4 text-black">
          <h3 className="text-lg font-semibold mb-2">災害時の行動指針</h3>
          <p className='text-black'>
            1. 落ち着いて状況を確認する<br />
            2. 安全な場所に避難する<br />
            3. 家族や周囲の人の安否を確認する<br />
            4. 正確な情報を入手する<br />
            5. 必要に応じて支援を求める
          </p>
        </div>
      </main>
    </div>
  );
};

export default MobilePage;