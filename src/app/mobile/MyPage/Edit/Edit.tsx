import { useState } from 'react';
import Link from 'next/link';

const UserEditPage = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  // 初期のユーザー情報
  const initialUserInfo = {
    myNumber: '1234567890123',
    name: '中村 勇士',
    gender: '男性',
    age: '26',
    address: '東京都新宿区西新宿2-8-1',
    phoneNumber: '03-1234-5678'
  };

  const [userInfo, setUserInfo] = useState(initialUserInfo);
  const [editedUserInfo, setEditedUserInfo] = useState(initialUserInfo);

  // const handleInputChange = (e) => {
  //   const { name, value } = e.target;
  //   setEditedUserInfo({ ...editedUserInfo, [name]: value });
  // };

  // const handleSubmit = (e) => {
  //   e.preventDefault();
  //   setUserInfo(editedUserInfo);
  //   alert('情報が更新されました。');
  // };

  // const handleCancel = () => {
  //   setEditedUserInfo(userInfo);
  //   alert('編集がキャンセルされました。');
  // };

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
        <h1 className="text-xl font-bold text-white">みえるーむ</h1>
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
                </ul>
              </nav>
            </div>
          </div>
        </div>
      )}

      {/* Main Content */}
      <main className="flex-grow mt-16 p-4 overflow-y-auto">
        <form /*onSubmit={handleSubmit}*/ className="bg-white rounded-lg shadow p-4">
          <h2 className="text-2xl font-semibold mb-4 text-black">ユーザー情報編集</h2>
          
          <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700">マイナンバー</label>
            <input
              type="text"
              name="myNumber"
              value={editedUserInfo.myNumber}
              // onChange={handleInputChange}
              className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
            />
          </div>

          <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700">氏名</label>
            <input
              type="text"
              name="name"
              value={editedUserInfo.name}
              // onChange={handleInputChange}
              className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
            />
          </div>

          <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700">性別</label>
            <input
              type="text"
              name="gender"
              value={editedUserInfo.gender}
              // onChange={handleInputChange}
              className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
            />
          </div>

          <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700">年齢</label>
            <input
              type="text"
              name="age"
              value={editedUserInfo.age}
              // onChange={handleInputChange}
              className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
            />
          </div>

          <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700">住所</label>
            <input
              type="text"
              name="address"
              value={editedUserInfo.address}
              // onChange={handleInputChange}
              className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
            />
          </div>

          <div className="mb-4">
            <label className="block text-sm font-medium text-gray-700">電話番号</label>
            <input
              type="text"
              name="phoneNumber"
              value={editedUserInfo.phoneNumber}
              // onChange={handleInputChange}
              className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
            />
          </div>

          <div className="flex justify-end space-x-4">
            <button
              type="button"
              // onClick={handleCancel}
              className="px-4 py-2 bg-gray-300 text-gray-700 rounded-md hover:bg-gray-400"
            ><Link href="/mobile/MyPage/view">
              キャンセル
            </Link></button>
            <button
              type="submit"
              className="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600"
            ><Link href="/mobile/MyPage/view">
              確定
            </Link></button>
          </div>
        </form>
      </main>
    </div>
  );
};

export default UserEditPage;