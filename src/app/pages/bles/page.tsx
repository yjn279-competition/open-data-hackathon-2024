"use client";  // Client Componentとして動作させる

import { useState } from 'react';

const Receiver = () => {
    const [deviceID, setDeviceID] = useState<string | null>(null);
    const [allDeviceInfo, setAllDeviceInfo] = useState<any[]>([]); // 取得したすべてのデバイス情報を保持
    const [showModal, setShowModal] = useState(false); // モーダル表示制御

    const handleClick = async () => {
        const mockID = "test_device_id_12345";
        const mockData = "battery_level:85%";

        setDeviceID(mockID);

        try {
            // POSTリクエストでデータを送信
            const postResponse = await fetch('http://localhost:8000/ble/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    device_id: mockID,
                    data: mockData,
                }),
            });

            if (!postResponse.ok) {
                throw new Error('サーバーエラー: ' + postResponse.statusText);
            }

            // POST送信後にGETリクエストですべてのデバイス情報を取得
            const getResponse = await fetch('http://localhost:8000/ble/');
            if (!getResponse.ok) {
                throw new Error('GETリクエストエラー: ' + getResponse.statusText);
            }
            const data = await getResponse.json();
            setAllDeviceInfo(data); // 取得した情報を保存
            setShowModal(true);  // モーダルを表示
        } catch (error) {
            console.error('エラー:', error);
        }
    };

    // モーダルを閉じる処理
    const closeModal = () => {
        setShowModal(false);
    };

    return (
        <div style={styles.container}>
            <h1 style={styles.heading}>仮データ受信</h1>
            <div id="idDisplay" style={styles.idDisplay}>
                {deviceID ? `受信したID: ${deviceID}` : 'IDを待機中...'}
            </div>
            <button
                id="connectButton"
                style={styles.connectButton}
                onClick={handleClick}
            >
                仮のBLEデータを送信
            </button>

            {/* モーダルウィンドウ */}
            {showModal && (
                <div style={styles.modal}>
                    <div style={styles.modalContent}>
                        <h2>すべてのデバイス情報</h2>
                        {allDeviceInfo.length > 0 ? (
                            <div>
                                <ul>
                                    {allDeviceInfo.map((device, index) => (
                                        <li key={index}>
                                            <p>ID: {device.device_id}</p>
                                            <p>データ: {device.data}</p>
                                        </li>
                                    ))}
                                </ul>
                            </div>
                        ) : (
                            <p>デバイス情報を読み込み中...</p>
                        )}
                        <button onClick={closeModal} style={styles.closeButton}>閉じる</button>
                    </div>
                </div>
            )}
        </div>
    );
};

export default Receiver;

// スタイルをオブジェクトとして定義
const styles = {
    container: {
        backgroundColor: '#f0f4f8',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        height: '100vh',
        margin: 0,
        padding: 0,
    },
    heading: {
        fontSize: '2rem',
        color: '#333',
    },
    idDisplay: {
        marginTop: '20px',
        padding: '15px',
        fontSize: '1.5rem',
        color: '#007acc',
        border: '1px solid #007acc',
        borderRadius: '8px',
        backgroundColor: '#e6f2ff',
        width: '80%',
        textAlign: 'center',
    },
    connectButton: {
        marginTop: '30px',
        padding: '10px 20px',
        fontSize: '1.2rem',
        color: '#fff',
        backgroundColor: '#007acc',
        border: 'none',
        borderRadius: '8px',
        cursor: 'pointer',
        transition: 'background-color 0.3s ease',
    },
    modal: {
        position: 'fixed',
        top: 0,
        left: 0,
        width: '100%',
        color: '#007acc',
        height: '100%',
        backgroundColor: 'rgba(0, 0, 0, 0.5)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
    },
    modalContent: {
        backgroundColor: '#fff',
        padding: '20px',
        borderRadius: '8px',
        textAlign: 'center',
        maxWidth: '500px',
        width: '100%',
    },
    closeButton: {
        marginTop: '20px',
        padding: '10px 20px',
        backgroundColor: '#007acc',
        color: '#fff',
        border: 'none',
        borderRadius: '8px',
        cursor: 'pointer',
    },
};
