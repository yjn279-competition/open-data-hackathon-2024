import { useState } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/router';

const Edit = () => {
  const router = useRouter();
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  // ダミーの初期ユーザー情報
  const initialUserInfo = {
    myNumber: '1234567890123',
    name: '山田 太郎',
    gender: '男性',
    age: '35',
    address: '東京都新宿区西新宿2-8-1',
    phoneNumber: '03-1234-5678'
  };

  const [userInfo, setUserInfo] = useState(initialUserInfo);

  const handleChange = (e) => {
    setUserInfo({ ...userInfo, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // ここで編集内容を保存する処理を実装
    // 実際のアプリケーションではAPIを呼び出すなどの処理を行う
    router.push('/user-info');
  };

  const handleCancel = () => {
    router.push('/user-info');
  };

  return (
    <div className="flex flex-col h-screen">
      {/* Header */}
      <header className="fixed top-0 left-0 right-0 bg-blue-500 text-white p-4 flex items-center z-10">
        <button
          onClick={() => setIsMenuOpen(!isMenuOpen)}
          className="text-2xl mr-4"
        >
          ☰
        </button>
        <h1 className="text-xl font-bold">ユーザー情報編集</h1>
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
                </ul>
              </nav>
            </div>
          </div>
        </div>
      )}

      {/* Main Content */}
      <main className="flex-grow mt-16 p-4 overflow-y-auto">
        <form onSubmit={handleSubmit} className="bg-white rounded-lg shadow p-4">
          <h2 className="text-2xl font-semibold mb-4">ユーザー情報編集</h2>
          <div className="space-y-4">
            <div>
              <label htmlFor="myNumber" className="block font-semibold mb-1">マイナンバー:</label>
              <input
                type="text"
                id="myNumber"
                name="myNumber"
                value={userInfo.myNumber}
                onChange={handleChange}
                className="w-full border rounded px-2 py-1"
              />
            </div>
            <div>
              <label htmlFor="name" className="block font-semibold mb-1">氏名:</label>
              <input
                type="text"
                id="name"
                name="name"
                value={userInfo.name}
                onChange={handleChange}
                className="w-full border rounded px-2 py-1"
              />
            </div>
            <div>
              <label htmlFor="gender" className="block font-semibold mb-1">性別:</label>
              <input
                type="text"
                id="gender"
                name="gender"
                value={userInfo.gender}
                onChange={handleChange}
                className="w-full border rounded px-2 py-1"
              />
            </div>
            <div>
              <label htmlFor="age" className="block font-semibold mb-1">年齢:</label>
              <input
                type="text"
                id="age"
                name="age"
                value={userInfo.age}
                onChange={handleChange}
                className="w-full border rounded px-2 py-1"
              />
            </div>
            <div>
              <label htmlFor="address" className="block font-semibold mb-1">住所:</label>
              <input
                type="text"
                id="address"
                name="address"
                value={userInfo.address}
                onChange={handleChange}
                className="w-full border rounded px-2 py-1"
              />
            </div>
            <div>
              <label htmlFor="phoneNumber" className="block font-semibold mb-1">電話番号:</label>
              <input
                type="text"
                id="phoneNumber"
                name="phoneNumber"
                value={userInfo.phoneNumber}
                onChange={handleChange}
                className="w-full border rounded px-2 py-1"
              />
            </div>
          </div>
          <div className="mt-6 flex justify-end space-x-4">
            <button
              type="button"
              onClick={handleCancel}
              className="bg-gray-300 text-gray-700 px-4 py-2 rounded"
            >
              キャンセル
            </button>
            <button
              type="submit"
              className="bg-blue-500 text-white px-4 py-2 rounded"
            >
              確定
            </button>
          </div>
        </form>
      </main>
    </div>
  );
};

export default Edit;